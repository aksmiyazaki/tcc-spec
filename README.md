## Glossário de termos da área
| Termo  | Descrição  |
|:--|:--|
| BSP applications | Bulk-synchronous parallel applications, abordagem comum quando trabalhando com ambientes homogêneos  |
|   |   |
### Notas sobre Analyzing Dynamic Task-Based applications on Hybrid Platforms: An Agile Scripting Approach
- Análise de aplicações _task-based_ em arquiteturas híbridas
- StarPU runtime system -> task parallelism runtime que objetiva explorar arqui
teturas híbridas, fornecendo uma extensão _MPI-based_ para explorar vários nós.
- Identificação de erros de alocação, problemas de prioridade em decisões de alo
cação, anomalias em tarefas de GPU e questões envolvendo caminho crítico.

- Devido a demanda de mais poder de processamento, é comum utilizar _nodes_
híbridos, compostos por processadores multicore, com múltiplas GPUs.
- Por causa da heterogeneidade e complexidade dessas máquinas, é comum surgirem
problemas de performance.
- Desenvolvido Framework para facilitar identificação de problemas de performan
ce, combinando R (ggplot2) e org-mode
- Há diversos _runtimes_ para executar aplicações _task-based_ (é importante enu
    merar alguns para a contextualização na proposta)
- BSP-based trace visualization tools - exemplos?
    - Vite
    - Paraver
    - Vampir - proprietary
- MPI é BSP-based, a maior parte das ferramentas de visualização focam nela.
- Técnicas comum é baseada em gráficos Gantt.
- Visualização para aplicações DAG
    - Construidas com recursos não projetados para análise de dados.
    - Baseiam-se ou em estratégias ou não escaláveis ou não baseadas em scripts
    (ex: com interações com mouse).
    - DAGViz
        - Representação visual de tarefas, focada na estrutura DAG, representan
        do de forma hierárquica
        - Obtida com a utilização de Macros (traduzido para Cilk, Intel TBB ou
            OpenMP)
        - Não há como obter dimensão de tempo e duração de tarefas, o que torna
        a análise de performance difícil.
    - Temanejo
        - Similar ao DAGViz (timeless DAG interativo)
        - Funcionalidade de debug
    - Haugen
        - Gannt com dependências
        - Não é escalável
        - Mostra apenas um nível de dependências (pode ser necessário diversos)
        níveis para entender o problema de escalonamento.
- Comportamento estocástico dificulta reproducibilidade
- Dependências entre tarefas são parte da aplicação e devem ser exploradas para
entender gargalos
- Traces desse domínio de aplicação são grandes, é necessário filtrar apenas da
dos relevantes
- É difícil de desenvolver algo _general purpose_ para cobrir todos os casos de
análise, motivação para fazer algo baseado em scripts
- Uma abordagem comum é avaliar traces de uma mesma aplicação rodando com dife
rentes escalonadores. Para analisar essas múltiplas execuções, é necessário sin
cronizar e filtrar os traces.
- Framework de visualização proposto, permite combinar de forma fácil e rápida
várias visualizações e propor visualizações alternativas de forma ágil.
- Workflow retirado do artigo (https://hal.inria.fr/hal-01353962v2/document)
![](./img/Workflow.png)
    1. StarPU converte traces FXT para reproduzir eventos com registro de data
    e hora na linguagem Paje.
    2. Também é criado um DAG com identificadores coerentes com o trace Paje.
    3. Utilizando pjdump, transforma-se os traces Paje em CSV que podem ser car
    regados em R.
    4. Para visualizações estáticas, utiliza-se ggplot2, para dinâmicas, utiliza
    -se plotly
