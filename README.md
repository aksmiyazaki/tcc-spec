# Objetivo

O objetivo deste trabalho foi adaptar o framework StarVZ para utilizar ferramentas
de Big Data para o pré-processamento de seus dados. Os resultados foram bem
promissores e podem ser consultados no [PDF da monografia](https://github.com/aksmiyazaki/tcc-spec/blob/master/Final.pdf).

O código fonte produzido neste trabalho está atualmente em um
[Fork do StarVZ](https://github.com/aksmiyazaki/starvz/tree/spark_starvz). Após
algum acabamento, é possível que ele vá para o repositório principal.

# Organização

Este repositório está organizado da seguinte forma:
  - dataframe_validation: contém as validações realizadas em uma carga de trabalho.
  Elas estão organizadas em pastas de acordo com sua tabela e dentro da pasta,
  há arquivos no formato _\<id\>\_\<tabela\>\_\<modo\_execução\>\_\<objeto\_da\_validação\>;
  - drawing: contém os arquivos vsdx de todas as figuras utilizadas no trabalho
  (Visio 2016);
  - env-setup: possui arquivos para auxiliar no setup de ambiente para realizar
  testes (voltado para o ambiente PCAD) da UFRGS;
  - experiments: dados de experimentos realizados, além de scripts para fazer o
  parse de seus logs;
  - final-text: contém a monografia (LaTeX);
  - notes: apenas anotações realizadas durante o trabalho;
  - proposal: contém a proposta do trabalho;
  - scripts: contém scripts diversos utilizados durante o trabalho;

# Reprodução dos testes
Atualmente, o Apêndice A da monografia contém instruções de como reproduzir os
testes realizados neste trabalho. Ele é reproduzido abaixo e o objetivo é que a
medida que o acabamento no pacote R evoluir, esta documentação será atualizada.

O Setup do ambiente para executar os experimentos começa com o script
setup\_environment.py, dentro da pasta scripts do repositório. É
necessário copiar também o script setup\_rpackages.R para o mesmo
diretório, pois este é chamado pelo primeiro.

Após executar o script setup\_environment.py para finalizar
a instalação do Hadoop é necessário:
  - Executar o comando source ~/.bashrc;
  - Verificar se o parâmetro fs.default.name no arquivo core-site.xml
   está configurado corretamente (deve apontar para o Namenode);
  - Verificar se o parâmetro dfs.replication no arquivo hdfs-site.xml está
  coerente. Nos experimentos, este foi definido como o número de nós;
  - Configurar o arquivo slaves, que basicamente lista todos os nós do cluster
  Hadoop.

Feito isso, é necessário realizar as configurações do Spark. Para isso, deve-se
configurar o arquivo slaves, da mesma forma que no Hadoop. Também é preciso
configurar os parâmetros SPARK\_LOCAL\_IP e SPARK\_MASTER\_HOST no arquivo
spark-env.sh, com o IP local e o IP do nó mestre respectivamente. Revise também
os parâmetros no arquivo spark-defaults.conf, pois há uma série de apontamentos
para o nó mestre.

Agora, vamos iniciar o Hadoop. Para isso, entre na pasta raiz de sua instalação
e execute a sequência de comandos listada abaixo.

```
hadoop namenode -format
./sbin/start-dfs.sh
```

Para garantir que ele está rodando, pode ser executado o comando hdfs
dfsadmin -report. Devem ser listados todos os datanodes do ambiente.

Agora, mude de diretório para onde estão os CSVs que serão utilizados como
entrada. Execute a sequência de comandos listada abaixo. Isso criará a pasta
logs e a pasta inputs no HDFS e copiará todos os arquivos CSV para a pasta
inputs. Este comando pode demorar.

```
hdfs dfs -mkdir -p logs
hdfs dfs -mkdir -p inputs
hdfs dfs -put * inputs/
```

Com o Hadoop rodando, iremos iniciar o Spark. Para isso, no nó mestre, execute
o seguinte comando: ./sbin/start-master.sh. Nos nós trabalhadores, o
comando é um pouco diferente: ./sbin/start-slave.sh <IP\_MASTER>:7077.

Se tudo ocorreu corretamente, agora temos o ambiente completo. Para executar o
StarVZ, vá até sua pasta e execute o seguinte comando:

```
./R/phase1-workflow.R -D /inputs <PATH_PARA_ENTITIES>
spark://<IP_MESTRE>:7077 cholesky
```

Este deve iniciar a aplicação em modo distribuído e rodar a aplicação
utilizando o Spark. Para repetições de testes, existe o script
experiment\_execution.py, que controla os experimentos, caso o
usuário queira executar mais de uma repetição do mesmo teste.


# Contato
- aksmiyazaki@gmail.com
