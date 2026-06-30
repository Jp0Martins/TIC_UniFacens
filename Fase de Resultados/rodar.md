# Para rodar a fase 9 automáticamente basta clicar no arquivo rodar.bat.

# Como rodar a Fase 9

## 1. Instalar dependências
```bash
pip install streamlit pandas duckdb plotly pyarrow
```

## 2. Preparar base do dashboard
```bash
python src/preparar_base_dashboard.py
```

## 3. Rodar o dashboard
```bash
streamlit run app/dashboard.py
```

## 4. Relatório final
O relatório final está em:

`relatorio/relatorio_final.md`