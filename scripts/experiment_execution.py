import subprocess
import os
from datetime import datetime

output_dir = "~/experiment_seq"
mode = "-S"
dir_input = "${SCRATCH}Workdir/inputs"
repetition_number = 1

def formatted_print(var):
    print(str(datetime.now()) + "   >>>>>>>> [" + var + "] <<<<<<<<")

def make_output_name(dir, iter):
    res = dir + "/experiment_" + f"{iter:02d}" + ".log"
    formatted_print("Output name is going to be [ " + res + " ]" )
    return res

formatted_print("STARTING EXPERIMENT BATCH")
for i in range(0,repetition_number):
    formatted_print("STARTING EXPERIMENT [ " + f"{i:02d}" + " ]")
    command = "${SCRATCH}Workdir/starvz/R/phase1-workflow.R -S " + dir_input + " cholesky"
    output_file = make_output_name(output_dir, i)
    full_command = command + " > " + output_file + " 2>&1"
    formatted_print("Running command: [ " + full_command + " ]")
    subprocess.run([full_command], shell=True)
    subprocess.run(["rm -rf "+ dir_input + "/*.parquet"], shell=True)
    formatted_print("EXPERIMENT [ " +  f"{i:02d}" + " ] DONE")
