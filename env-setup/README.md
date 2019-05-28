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
    - Setando hadoop no master
        - echo "export JAVA_HOME=$(spack location -i jdk)" >> ~/.bashrc
        - echo "export PATH=$PATH:$(spack location -i hadoop)/bin" >> ~/.bashrc
        - source ~/.bashrc
        - core-site.xml setado
        - hdfs-site.xml setado
        - mapred-site.xml setado
        - yarn-site.xml setado
        - Arquivo slaves:  
            `node-slave1`  
            `node-slave2`
    - Setando hadoop nos slaves
        - Todos os arquivos do master diretório etc/hadoop/ copiados para os slaves
        - Setando variaveis
            - echo "export JAVA_HOME=$(spack location -i jdk)" >> ~/.bashrc
            - echo "export PATH=$PATH:$(spack location -i hadoop)/bin" >> ~/.bashrc
            - source ~/.bashrc
    - Novamente no master: hdfs namenode -format
    - hdfs dfs -mkdir /spark-logs


## Setando Spark


export PATH=$PATH:/home/admin/spack/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/home/admin/spack/bin/
export JAVA_HOME=/home/admin/spack/opt/spack/linux-debian9-x86_64/gcc-6.3.0/jdk-11.0.2_9-rpc4uiglauqzga3qk4dcfies66nujiks
export PATH=$PATH:/home/admin/spack/opt/spack/linux-debian9-x86_64/gcc-6.3.0/hadoop-2.9.0-e6gqhu36bmugq3hyiqrcfrqcllpekq4j/bin
export PATH=$PATH:/home/admin/spack/opt/spack/linux-debian9-x86_64/gcc-6.3.0/spark-2.3.0-ylcznu3poqpmcnrl7eq4parfywjrd2zd/bin
export SPARK_HOME=/home/admin/spack/opt/spack/linux-debian9-x86_64/gcc-6.3.0/spark-2.3.0-ylcznu3poqpmcnrl7eq4parfywjrd2zd
export PATH=$PATH:$JAVA_HOME/bin


https://www.linode.com/docs/databases/hadoop/how-to-install-and-set-up-hadoop-cluster/#format-hdfs
https://www.linode.com/docs/databases/hadoop/install-configure-run-spark-on-top-of-hadoop-yarn-cluster/
