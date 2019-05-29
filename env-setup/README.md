# Anotações sobre o setup de ambiente de desenvolvimento

## Setando Hadoop
- Realizado deploy de 3 nodes Debian Stretch com instâncias t2micro na amazon
EC2.
- ssh -i <chave> admin@<amazon_instance>
- Ao acessar a instância
    - sudo apt-get update; sudo apt-get install git -y; git clone https://github.com/spack/spack.git; source ./spack/share/spack/setup-env.sh;
    - echo "export PATH=$PATH:$HOME/spack/bin/" >> ~/.bashrc; sudo apt-get install build-essential -y;
    - spack install -y hadoop@2.9.0; spack install -y spark
    - Adicionado no início do arquivo /etc/hosts:  
        `172.31.13.5	node-master`  
        `172.31.10.137	node-slave1`  
        `172.31.12.249	node-slave2`
    - Copiadas chaves ssh para ~/.ssh
        - wget https://www.dropbox.com/s/l0g5vx5tn3vueg2/kp_amazon_internal.tar.gz?dl=1; mv kp_amazon_internal.tar.gz\?dl\=1 kp_amazon.tar.gz;tar -xvf kp_amazon.tar.gz; mv kp/* ~/.ssh/;cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
    - Variáveis de ambiente:
        - Tendo em vista que o SPACK está no PATH, colocar o seguinte no bashrc
        - export PATH=$PATH:$(spack location -i hadoop)/bin
        - export JAVA_HOME=$(spack location -i jdk)
        - export PATH=$PATH:$(spack location -i spark)/bin
        - export SPARK_HOME=$(spack location -i spark)
        - export PATH=$PATH:$JAVA_HOME/bin
    - Setando hadoop no master
        - setar core-site.xml (exemplo em env-setup/hadoop, deve ser colocado em hadoop/etc/hadoop)
        - setar hdfs-site.xml (exemplo em env-setup/hadoop, deve ser colocado em hadoop/etc/hadoop)
        - setar mapred-site.xml (exemplo em env-setup/hadoop, deve ser colocado em hadoop/etc/hadoop)
        - setar yarn-site.xml (exemplo em env-setup/hadoop, deve ser colocado em hadoop/etc/hadoop)
        - setar a variável JAVA_HOME no arquivo hadoop-env.sh (exemplo em env-setup/hadoop, deve ser colocado em hadoop/etc/hadoop)
        - setar arquivo slaves com os nomes do /etc/hosts:  
            `node-slave1`  
            `node-slave2`
        - setar .profile (exemplo em env-setup/hadoop, no diretório raiz do hadoop)
    - Setando hadoop nos slaves
        - Editar bashrc para ter mesmas variáveis de ambiente.
        - Copiar arquivos de configuração do master.

    - Novamente no master: hdfs namenode -format
    - Iniciar hdfs (do diretório do hadoop)
        - ./sbin/start-dfs.sh
        - Confirmar que dfs está rodando (via <ip_master>:50070 ou comando hdfs dfsadmin -report)
        - Também confirmar que processos estão rodando com jps
        - ./sbin/start-yarn.sh
        - Confirmar que yarn está rodando (via <ip_master>:8088)

## Setando Spark
    - Editar o arquivo spark-defaults.conf (exemplo em spark-defaults.conf). Arquivo fica em $SPARK_HOME/conf (existe apenas um template lá).
    - Criar um diretório para logs no hdfs
        - hdfs dfs -mkdir /spark-logs
    - 



https://www.linode.com/docs/databases/hadoop/how-to-install-and-set-up-hadoop-cluster/#format-hdfs
https://www.linode.com/docs/databases/hadoop/install-configure-run-spark-on-top-of-hadoop-yarn-cluster/
