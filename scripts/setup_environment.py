import subprocess
import os

node_memory_size = 64000

print('Starting environment setup')
scratch_dir = os.environ['SCRATCH']
os.chdir(scratch_dir)
print('Current Directory ' + os.getcwd())

#print('Clonning Spack')
#subprocess.run(["git clone https://github.com/spack/spack.git"])

#print('Setting Spack')
#subprocess.run(["source ./spack/share/spack/setup-env.sh"])
#subprocess.run(['echo "export PATH=\$PATH:\$HOME/Spack/bin/" >> ~/.bashrc'])
#subprocess.run(["source ~/.bashrc"])

work_dir = scratch_dir + '/Workdir'
print('Going to workdir')

if not os.path.exists(work_dir):
    os.makedirs(work_dir)
    os.chdir("./Workdir")
    print('Current Directory ' + os.getcwd())

    print('Getting hadoop from the web')
    subprocess.call(["wget https://archive.apache.org/dist/hadoop/common/hadoop-2.9.0/hadoop-2.9.0.tar.gz"], shell=True)
    subprocess.run(["tar -xvf hadoop-2.9.0.tar.gz"], shell=True)
    subprocess.run(["rm hadoop-2.9.0.tar.gz"], shell=True)

    print('Downloading Hadoop Configuration')
    subprocess.run(["wget https://www.dropbox.com/s/sfc6bzohpcainyu/env-setup.tar.gz?dl=1"], shell=True)
    subprocess.run(["mv 'env-setup.tar.gz?dl=1' env-setup.tar.gz"], shell=True)
    subprocess.run(["tar -xvf env-setup.tar.gz"], shell=True)
    subprocess.run(["rm env-setup.tar.gz"], shell=True)
    subprocess.run(["mv env-setup/hadoop/.profile hadoop-2.9.0/"], shell=True)
    subprocess.run(["mv env-setup/hadoop/* hadoop-2.9.0/etc/hadoop/"], shell=True)

    ### HADOOP CONFIGURATION STARTS HERE
    print('Changing Hadoop Configuration Files')
    subprocess.run(["sed -i 's+hadoop/data/namenode/+\\/scratch/aksmiyazaki/data/namenode+g' hadoop-2.9.0/etc/hadoop/hdfs-site.xml"], shell=True)
    subprocess.run(["sed -i 's+hadoop/data/dataNode+\\/scratch/aksmiyazaki/data/datanode+g' hadoop-2.9.0/etc/hadoop/hdfs-site.xml"], shell=True)
    subprocess.run(["sed -i 's+<value>hdfs://node-master:9000</value>+<value>hdfs://127.0.0.1:9000</value>+g' hadoop-2.9.0/etc/hadoop/core-site.xml"], shell = True)
    subprocess.run(["sed -i 's+export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre+export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre+g' hadoop-2.9.0/etc/hadoop/hadoop-env.sh"], shell=True)
    subprocess.run(["sed -i 's+export HADOOP_CONF_DIR=/home/admin/spack/opt/spack/linux-debian9-x86_64/gcc-6.3.0/hadoop-2.9.0-e6gqhu36bmugq3hyiqrcfrqcllpekq4j/etc/hadoop+export HADOOP_CONF_DIR=\${SCRATCH}Workdir/hadoop-2.9.0/etc/hadoop+g' hadoop-2.9.0/.profile"], shell=True)
    subprocess.run(["sed -i 's+export LD_LIBRARY_PATH=/home/admin/spack/opt/spack/linux-debian9-x86_64/gcc-6.3.0/hadoop-2.9.0-e6gqhu36bmugq3hyiqrcfrqcllpekq4j/lib/native:$LD_LIBRARY_PATH+export LD_LIBRARY_PATH=\${SCRATCH}Workdir/hadoop-2.9.0/lib/native:$LD_LIBRARY_PATH+g' hadoop-2.9.0/.profile"], shell=True)
    subprocess.run(['echo "JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre" >> ~/.bashrc'], shell=True)
    subprocess.run(['echo "PATH=\$PATH:\${SCRATCH}Workdir/hadoop-2.9.0/bin:\${SCRATCH}Workdir/hadoop-2.9.0/sbin" >> ~/.bashrc'], shell=True)
    subprocess.run(['source ~/.bashrc'], shell=True)

    ### SPARK CONFIGURATION STARTS HERE
    print("Configuring Spark")
    subprocess.run(["wget https://archive.apache.org/dist/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz"], shell=True)
    subprocess.run(["tar -xvf spark-2.4.3-bin-hadoop2.7.tgz"], shell=True)
    subprocess.run(["rm -rf spark-2.4.3-bin-hadoop2.7.tgz"], shell=True)
    subprocess.run(["cp env-setup/spark/* spark-2.4.3-bin-hadoop2.7/conf"], shell=True)
    subprocess.run(["sed -i 's+export HADOOP_CONF_DIR=/home/aksmiyazaki/Spack/opt/spack/linux-debian9-x86_64/gcc-6.3.0/hadoop-2.9.0-e6gqhu36bmugq3hyiqrcfrqcllpekq4j/etc/hadoop+export HADOOP_CONF_DIR=/scratch/aksmiyazaki/Workdir/hadoop-2.9.0/etc/hadoop+g' spark-2.4.3-bin-hadoop2.7/conf/spark-env.sh"], shell=True)
    subprocess.run(['echo "SPARK_HOME=${SCRATCH}Workdir/spark-2.4.3-bin-hadoop2.7" >> ~/.bashrc'], shell=True)


    ### Personal Stuff
    print("Configuring R-Package")
    subprocess.run(["wget https://www.dropbox.com/s/9r2436s7xkd7qbj/spark-startvz.tar.gz?dl=1"], shell=True)
    subprocess.run(["mv 'spark-startvz.tar.gz?dl=1' spark-starvz.tar.gz"], shell=True)
    subprocess.run(["tar -xvf spark-starvz.tar.gz"], shell=True)
    subprocess.run(["rm -rf spark-starvz.tar.gz"], shell=True)

    print("Copying inputs")
    subprocess.run(["mkdir inputs"], shell=True)
    subprocess.run(["cp ~/data/post-process-unzip/6-v2_chifflet_4_24_2_DMDAS_dpotrf_2_360000_1440_false_false.dir/6-v2_chifflet_4_24_2_DMDAS_dpotrf_2_360000_1440_false_false_fxt/* inputs/"], shell=True)

    print("Running r package installer")
    subprocess.run(["chmod 777 setup_rpackages.R"], shell=True)
    subprocess.run(["./setup_rpackages.R"], shell=True)
else:
    subprocess.run(['source ~/.bashrc'], shell=True)






print('Dont forget to: ')
print('CONFIGURE MAPRED-SITE')
print('app.mapreduce.am = 8192, mapreduce.map = 4096, mapreduce.reduce=8192')
print('On CORE-SITE, param must be set to the master IP')
print('SET SLAVES FILE')

print('CONFIGURE YARN-SITE')
print('SET RESOURCEMANAGER TO MASTER ADDRESS')
print('yarn.nodemanager.resource.memory-mb = 61000, yarn.scheduler.maximum-allocation-mb=610000, yarn.scheduler.minimum-allocation-mb=512')
print('Configure SPARK-ENV.SH')

print('Check ~/.bashrc file.')

print('EDIT slaves FILE')
