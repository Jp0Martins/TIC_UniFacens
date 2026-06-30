from pathlib import Path
import pandas as pd
import duckdb

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "input"
PROCESSED_DIR = BASE_DIR / "processed"

RESUMO_FILE = INPUT_DIR / "resumo_executivo_periodo.csv"
COMPARATIVO_CENARIOS_FILE = INPUT_DIR / "comparativo_cenarios.csv"
FLUXOS_OD_FILE = INPUT_DIR / "fluxos_od.parquet"
MARKOV_PROB_FILE = INPUT_DIR / "matriz_markov_probabilidade.parquet"

KPIS_FILE = PROCESSED_DIR / "kpis_gerais.csv"
BASES_DOC_FILE = PROCESSED_DIR / "bases_dashboard.md"


def main():
    for arquivo in [
        RESUMO_FILE,
        COMPARATIVO_CENARIOS_FILE,
        FLUXOS_OD_FILE,
        MARKOV_PROB_FILE,
    ]:
        if not arquivo.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    con = duckdb.connect()

    resumo = pd.read_csv(RESUMO_FILE)
    comparativo = pd.read_csv(COMPARATIVO_CENARIOS_FILE)

    total_fluxos = resumo["total_fluxos"].sum()
    total_inter = resumo["fluxos_inter"].sum()
    total_intra = resumo["fluxos_intra"].sum()

    total_periodos = resumo["periodo_dia"].nunique()

    total_fluxos_od = con.execute(f"""
        SELECT COUNT(*) FROM read_parquet('{FLUXOS_OD_FILE}')
    """).fetchone()[0]

    total_markov = con.execute(f"""
        SELECT COUNT(*) FROM read_parquet('{MARKOV_PROB_FILE}')
    """).fetchone()[0]

    kpis = pd.DataFrame(
        [
            {
                "total_fluxos_resumidos": total_fluxos,
                "total_fluxos_intra": total_intra,
                "total_fluxos_inter": total_inter,
                "total_periodos": total_periodos,
                "total_fluxos_od_agregados": total_fluxos_od,
                "total_transicoes_markov_agregadas": total_markov,
                "cenario_recomendado": "B_2mais_eventos",
            }
        ]
    )

    kpis.to_csv(KPIS_FILE, index=False)

    texto = f"""# Bases do Dashboard

## Arquivos de entrada utilizados
- resumo_executivo_periodo.csv
- top_fluxos_interzona.csv
- top_markov_interzona.csv
- destinos_alternativos.csv
- comparativo_cenarios.csv
- comparativo_periodo.csv
- recomendacao_cenario.csv
- matriz_od_absoluta.parquet
- matriz_od_probabilidade.parquet
- fluxos_od.parquet
- modelo_prob_od.parquet
- matriz_markov_probabilidade.parquet

## KPI principal consolidado
- Total de fluxos resumidos: {int(total_fluxos):,}
- Total intra-zona: {int(total_intra):,}
- Total inter-zona: {int(total_inter):,}
- Total de períodos: {int(total_periodos)}
- Total de fluxos O-D agregados: {int(total_fluxos_od)}
- Total de transições Markov agregadas: {int(total_markov)}

## Cenário metodológico recomendado
- B_2mais_eventos
"""

    BASES_DOC_FILE.write_text(texto, encoding="utf-8")

    print("KPIs gerais:")
    print(kpis.to_string(index=False))
    print(f"\nArquivo gerado: {KPIS_FILE}")
    print(f"Arquivo gerado: {BASES_DOC_FILE}")
    print("\nPreparação da base do dashboard concluída.")


if __name__ == "__main__":
    main()
