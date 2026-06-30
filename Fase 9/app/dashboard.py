from pathlib import Path
import pandas as pd
import duckdb
import streamlit as st
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "input"
PROCESSED_DIR = BASE_DIR / "processed"

RESUMO_FILE = INPUT_DIR / "resumo_executivo_periodo.csv"
TOP_FLUXOS_FILE = INPUT_DIR / "top_fluxos_interzona.csv"
TOP_MARKOV_FILE = INPUT_DIR / "top_markov_interzona.csv"
DESTINOS_ALT_FILE = INPUT_DIR / "destinos_alternativos.csv"
COMP_CENARIOS_FILE = INPUT_DIR / "comparativo_cenarios.csv"
COMP_PERIODO_FILE = INPUT_DIR / "comparativo_periodo.csv"
RECOMENDACAO_FILE = INPUT_DIR / "recomendacao_cenario.csv"

MATRIZ_OD_ABS_FILE = INPUT_DIR / "matriz_od_absoluta.parquet"
MATRIZ_OD_PROB_FILE = INPUT_DIR / "matriz_od_probabilidade.parquet"
FLUXOS_OD_FILE = INPUT_DIR / "fluxos_od.parquet"
MODELO_PROB_OD_FILE = INPUT_DIR / "modelo_prob_od.parquet"
MARKOV_PROB_FILE = INPUT_DIR / "matriz_markov_probabilidade.parquet"

KPIS_FILE = PROCESSED_DIR / "kpis_gerais.csv"


@st.cache_data
def load_csv(path):
    return pd.read_csv(path)


@st.cache_data
def load_parquet(path):
    con = duckdb.connect()
    df = con.execute(f"SELECT * FROM read_parquet('{path}')").fetchdf()
    con.close()
    return df


def format_int(value):
    try:
        return f"{int(value):,}".replace(",", ".")
    except Exception:
        return str(value)


st.set_page_config(page_title="Dashboard de Mobilidade Urbana", layout="wide")

st.title("Dashboard de Mobilidade Urbana")
st.caption(
    "Projeto de análise de mobilidade urbana com matriz O-D, modelagem probabilística, "
    "transições Markovianas e avaliação de robustez metodológica."
)

kpis = load_csv(KPIS_FILE)
resumo = load_csv(RESUMO_FILE)
top_fluxos = load_csv(TOP_FLUXOS_FILE)
top_markov = load_csv(TOP_MARKOV_FILE)
destinos_alt = load_csv(DESTINOS_ALT_FILE)
comp_cenarios = load_csv(COMP_CENARIOS_FILE)
comp_periodo = load_csv(COMP_PERIODO_FILE)
recomendacao = load_csv(RECOMENDACAO_FILE)

matriz_abs = load_parquet(MATRIZ_OD_ABS_FILE)
matriz_prob = load_parquet(MATRIZ_OD_PROB_FILE)
fluxos_od = load_parquet(FLUXOS_OD_FILE)
modelo_prob = load_parquet(MODELO_PROB_OD_FILE)
markov_prob = load_parquet(MARKOV_PROB_FILE)

st.sidebar.header("Navegação")
pagina = st.sidebar.radio(
    "Selecione a página",
    [
        "Apresentação do Projeto",
        "Visão Geral",
        "Matriz O-D",
        "Fluxos Inter-Zona",
        "Modelo Probabilístico",
        "Markov",
        "Robustez",
    ],
)

if pagina == "Apresentação do Projeto":
    st.subheader("O que este projeto fez")
    st.markdown("""
        Este projeto analisou registros de sensores viários para entender como os veículos
        se deslocam entre regiões da cidade ao longo do dia.

        A partir desses dados, foi possível transformar eventos brutos de passagem em
        informações mais úteis para análise urbana, como:

        - origem e destino por período do dia;
        - fluxos entre zonas;
        - probabilidades de deslocamento;
        - transições entre regiões;
        - padrões recorrentes de mobilidade.
        """)

    st.subheader("Principais entregas")
    st.markdown("""
        - Matriz Origem-Destino por período;
        - Identificação dos principais fluxos entre zonas;
        - Análise de horários com maior movimento;
        - Modelo probabilístico de destinos;
        - Cadeia de transição entre zonas (Markov);
        - Avaliação de robustez metodológica;
        - Dashboard interativo para consulta dos resultados.
        """)

    st.subheader("Métricas de avaliação consideradas")
    st.markdown("""
        A avaliação do projeto foi feita principalmente de forma qualitativa, considerando:

        - se os fluxos fazem sentido no contexto urbano;
        - se existe coerência temporal;
        - se os resultados são interpretáveis;
        - se os padrões encontrados geram insights úteis.

        Exemplos de coerência esperada:
        - manhã e tarde com maior intensidade de deslocamentos;
        - fluxos recorrentes entre determinadas regiões;
        - padrões consistentes em múltiplos períodos do dia.
        """)

    st.subheader("Principais achados")
    st.markdown("""
        Com base nos resultados obtidos:

        - a **tarde** foi o período com maior volume de deslocamentos;
        - o fluxo **Zona 3 → Zona 1** apareceu como principal corredor inter-zona;
        - conexões como **Zona 4 → Zona 2** e **Zona 1 → Zona 5** também se destacaram;
        - os padrões principais permaneceram estáveis em diferentes cenários metodológicos;
        - isso indica que os resultados são coerentes, interpretáveis e úteis para análise urbana.
        """)

    c1, c2, c3 = st.columns(3)
    c1.metric(
        "Total de fluxos analisados", format_int(kpis.loc[0, "total_fluxos_resumidos"])
    )
    c2.metric("Fluxos inter-zona", format_int(kpis.loc[0, "total_fluxos_inter"]))
    c3.metric("Períodos analisados", format_int(kpis.loc[0, "total_periodos"]))

    st.subheader("Resultados esperados alcançados")
    st.markdown("""
        O projeto conseguiu entregar os resultados esperados definidos para a atividade:

        - matriz origem-destino por período;
        - identificação de fluxos predominantes;
        - análise de variação temporal;
        - identificação de comportamentos recorrentes;
        - dashboard interativo como produto final analítico.
        """)

    st.subheader("Impacto prático")
    st.markdown("""
        Os resultados podem apoiar:

        - identificação de corredores de tráfego mais utilizados;
        - apoio a decisões de transporte público;
        - melhoria do planejamento urbano;
        - análise de padrões de mobilidade por período;
        - simulação de cenários em gêmeos digitais.
        """)

    st.subheader("Onde entra Inteligência Artificial neste projeto")
    st.markdown("""
        Este projeto usa uma abordagem híbrida de **IA + modelagem analítica**, adequada
        para dados incompletos e sem rótulos.

        A estratégia adotada combina:

        **1. Pré-processamento**
        - ordenação por veículo e tempo;
        - construção de sequências de leitura.

        **2. Clusterização espacial**
        - agrupamento de sensores em zonas urbanas;
        - redução da granularidade e aumento da interpretabilidade.

        **3. Inferência de trajetórias**
        - origem = primeira aparição observada;
        - destino = última aparição observada;
        - uso de frequência de transições para estimar deslocamentos.

        **4. Modelagem probabilística**
        - estimação de `P(destino | origem, horário)`;
        - tratamento de incerteza em dados incompletos.

        **5. Cadeias de Markov**
        - modelagem da próxima zona observada com base na zona atual;
        - representação sequencial da mobilidade.
        """)

    st.info("""
        Mesmo sem redes neurais ou aprendizado supervisionado, o projeto utiliza técnicas
        clássicas de IA e modelagem probabilística. Essa escolha foi adequada porque os
        dados são incompletos, não possuem rótulos e exigem interpretabilidade.
        """)

    st.subheader("Pequeno resumo de como IA pode ser aplicada com esses dados")
    st.markdown("""
        Com os dados disponíveis, a IA pode ser aplicada de forma **não supervisionada** e
        **probabilística**, sem necessidade de rótulos manuais.

        Já foi possível aplicar:
        - clusterização espacial;
        - inferência de origem e destino;
        - modelagem probabilística;
        - transições Markovianas.

        E futuramente seria possível evoluir para:
        - previsão do próximo destino;
        - classificação de perfis de mobilidade;
        - detecção de comportamentos anômalos;
        - simulação de cenários urbanos;
        - integração com gêmeos digitais.
        """)

    st.subheader("Limitações")
    st.markdown("""
        - os sensores observam apenas pontos específicos da cidade;
        - não há trajetória completa de todos os veículos;
        - muitas sessões possuem apenas um único evento;
        - parte da diagonal intra-zona reflete limitação observacional.

        Ainda assim, os resultados mostraram padrões consistentes e úteis para análise de
        mobilidade urbana.
        """)

elif pagina == "Visão Geral":
    st.subheader("Indicadores gerais")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total de fluxos", format_int(kpis.loc[0, "total_fluxos_resumidos"]))
    c2.metric("Fluxos intra-zona", format_int(kpis.loc[0, "total_fluxos_intra"]))
    c3.metric("Fluxos inter-zona", format_int(kpis.loc[0, "total_fluxos_inter"]))
    c4.metric("Cenário recomendado", kpis.loc[0, "cenario_recomendado"])

    st.subheader("Resumo executivo por período")
    st.dataframe(resumo, use_container_width=True)

    fig = px.bar(
        resumo,
        x="periodo_dia",
        y=["fluxos_intra", "fluxos_inter"],
        title="Fluxos intra e inter-zona por período",
        barmode="group",
    )
    st.plotly_chart(fig, use_container_width=True)

elif pagina == "Matriz O-D":
    st.subheader("Matriz O-D")

    periodo = st.selectbox(
        "Selecione o período",
        sorted(matriz_abs["periodo_dia"].unique()),
    )
    tipo = st.radio("Tipo de matriz", ["Absoluta", "Probabilidade"], horizontal=True)

    df = matriz_abs if tipo == "Absoluta" else matriz_prob
    df = df[df["periodo_dia"] == periodo].copy()

    st.dataframe(df, use_container_width=True)

    df_long = df.melt(
        id_vars=["periodo_dia", "zona_origem"],
        var_name="zona_destino",
        value_name="valor",
    )
    df_long["zona_destino"] = df_long["zona_destino"].astype(str)

    heatmap_data = df_long.pivot(
        index="zona_origem", columns="zona_destino", values="valor"
    )

    fig = px.imshow(
        heatmap_data,
        text_auto=".2f" if tipo == "Probabilidade" else True,
        aspect="auto",
        color_continuous_scale="YlOrRd",
        title=f"Matriz O-D {tipo} - {periodo}",
    )
    st.plotly_chart(fig, use_container_width=True)

elif pagina == "Fluxos Inter-Zona":
    st.subheader("Principais fluxos inter-zona")

    periodo_sel = st.selectbox(
        "Filtrar por período",
        ["Todos"] + sorted(top_fluxos["periodo_dia"].unique().tolist()),
    )

    df = top_fluxos.copy()
    if periodo_sel != "Todos":
        df = df[df["periodo_dia"] == periodo_sel]

    st.dataframe(df, use_container_width=True)

    fig = px.bar(
        df.sort_values("qtd_fluxos", ascending=True),
        x="qtd_fluxos",
        y="label_fluxo",
        orientation="h",
        title="Top fluxos inter-zona",
    )
    st.plotly_chart(fig, use_container_width=True)

elif pagina == "Modelo Probabilístico":
    st.subheader("Destino mais provável por origem e período")

    periodo = st.selectbox("Período", sorted(modelo_prob["periodo_dia"].unique()))
    origem = st.selectbox("Zona de origem", sorted(modelo_prob["zona_origem"].unique()))

    df = modelo_prob[
        (modelo_prob["periodo_dia"] == periodo) & (modelo_prob["zona_origem"] == origem)
    ].sort_values("rank_destino")

    st.dataframe(df, use_container_width=True)

    fig = px.bar(
        df,
        x="zona_destino",
        y="prob_destino_dado_origem",
        title=f"Distribuição de destinos | origem={origem} | período={periodo}",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Destinos alternativos")
    st.dataframe(destinos_alt, use_container_width=True)

elif pagina == "Markov":
    st.subheader("Matriz de transição Markov")

    periodo = st.selectbox(
        "Selecione o período",
        sorted(markov_prob["periodo_dia"].unique()),
    )

    df = markov_prob[markov_prob["periodo_dia"] == periodo].copy()
    st.dataframe(df, use_container_width=True)

    heatmap_data = df.pivot(
        index="zona_atual",
        columns="proxima_zona",
        values="prob_proxima_zona",
    )

    fig = px.imshow(
        heatmap_data,
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale="Blues",
        title=f"Matriz Markov Probabilística - {periodo}",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top transições Markov inter-zona")
    st.dataframe(top_markov, use_container_width=True)

elif pagina == "Robustez":
    st.subheader("Comparação entre cenários")
    st.dataframe(comp_cenarios, use_container_width=True)

    fig1 = px.bar(
        comp_cenarios,
        x="cenario",
        y="total_pares",
        title="Total de pares por cenário",
    )
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.bar(
        comp_cenarios,
        x="cenario",
        y="pct_interzona",
        title="% inter-zona por cenário",
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Distribuição por período")
    st.dataframe(comp_periodo, use_container_width=True)

    fig3 = px.bar(
        comp_periodo,
        x="periodo_dia",
        y="total_pares",
        color="cenario",
        barmode="group",
        title="Distribuição por período e cenário",
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Recomendação metodológica")
    st.dataframe(recomendacao, use_container_width=True)
