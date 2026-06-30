# Relatório Final — Mobilidade Urbana a partir de Sensores Viários

## 1. Objetivo do projeto
Construir um pipeline analítico para transformar registros de sensores viários em uma representação estruturada da mobilidade urbana, incluindo fluxos origem-destino, probabilidades de deslocamento, transições Markovianas e avaliação de robustez metodológica.

## 2. Etapas do projeto
- Fase 1: limpeza e padronização
- Fase 2: análise temporal por placa
- Fase 3: clusterização espacial dos sensores
- Fase 4: definição de sessões O-D
- Fase 5: matriz O-D absoluta e probabilística
- Fase 6: modelagem probabilística e Markov
- Fase 7: visualização e consolidação
- Fase 8: robustez metodológica
- Fase 9: dashboard e relatório final

## 3. Principais resultados
- mais de 15,5 milhões de pares O-D
- 5 zonas espaciais
- 4 períodos do dia
- principais fluxos inter-zona concentrados em 3→1, 4→2, 1→5
- forte dominância intra-zona, explicada em parte por sessões com 1 evento
- robustez dos principais fluxos mesmo sob diferentes cenários

## 4. Principal conclusão metodológica
O critério de sessões com 2 ou mais eventos apresentou melhor equilíbrio entre volume analítico e coerência interpretativa, sendo o cenário recomendado para análises mais refinadas de deslocamento.

## 5. Produto final
O projeto entrega:
- pipeline analítico completo
- matrizes O-D
- modelo probabilístico
- cadeia de Markov
- visualizações estáticas
- dashboard interativo
- avaliação de robustez

## 6. Trabalhos futuros
- incorporar mapa geográfico
- adicionar filtros por dia da semana
- separar dias úteis e finais de semana
- testar quebra de sessão por gap temporal
- prever próximo destino com base no estado atual