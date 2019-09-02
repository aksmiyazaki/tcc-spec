import subprocess
import os

print('Starting environment setup')
scratch_dir = os.environ['SCRATCH']
os.chdir(scratch_dir)
print('Current Directory ' + os.getcwd())


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
    subprocess.run(["wget -O env-setup.tar.gz https://www.dropbox.com/s/f94fc6ie8br80y6/env-setup.tar.gz?dl=1"], shell=True)
    subprocess.run(["tar -xvf env-setup.tar.gz"], shell=True)
    subprocess.run(["rm env-setup.tar.gz"], shell=True)
    subprocess.run(["mv env-setup/hadoop/.profile hadoop-2.9.0/"], shell=True)
    subprocess.run(["mv env-setup/hadoop/* hadoop-2.9.0/etc/hadoop/"], shell=True)

    ### HADOOP CONFIGURATION STARTS HERE
    print('Changing Hadoop Configuration Files')
    subprocess.run(['echo "JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre" >> ~/.bashrc'], shell=True)
    subprocess.run(['echo "PATH=\$PATH:\${SCRATCH}Workdir/hadoop-2.9.0/bin:\${SCRATCH}Workdir/hadoop-2.9.0/sbin" >> ~/.bashrc'], shell=True)



    os.chdir(work_dir)
    subprocess.run(["git clone https://github.com/aksmiyazaki/starvz.git"], shell=True)
    os.chdir(work_dir + '/starvz')
    subprocess.run(["git checkout spark_starvz"], shell=True)

    os.chdir(scratch_dir)
    print('Current Directory ' + os.getcwd())
    print("Running r package installer")
    subprocess.run(["chmod 777 setup_rpackages.R"], shell=True)
    subprocess.run(["./setup_rpackages.R"], shell=True)

    os.chdir(work_dir)
    subprocess.run(["mv env-setup/spark/slaves spark-2.4.3-bin-hadoop2.7/conf/"], shell=True)
    subprocess.run(["mv env-setup/spark/spark-defaults.conf spark-2.4.3-bin-hadoop2.7/conf/"], shell=True)
    subprocess.run(["mv env-setup/spark/spark-env.sh spark-2.4.3-bin-hadoop2.7/conf/"], shell=True)


print('DONE DONE DONE')
