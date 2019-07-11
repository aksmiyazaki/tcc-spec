output_directory = ""
mode = "-D"
input_directory_list = [("inputs", "/home/aksmiyazaki/tcc_data/5-v8-4_chifflet_8_6_2_dmdas_dpotrf_4_96000_960_false_ETHERNET10GB_true_r21909_10.dir/5-v8-4_chifflet_8_6_2_dmdas_dpotrf_4_96000_960_false_ETHERNET10GB_true_r21909_10_fxt")] # Input list, pairs in format <hdfs_dir>,<local_dir>
repetition_number = 1

input_directory_list[0][1]

for idl in range(0, len(input_directory_list)):
    for i in range(0,repetition_number):
        command = ""
        if mode == "-D":
            command = "./phase1-workflow.R -D " + input_directory_list[idl][0] + " " + input_directory_list[idl][1] + " yarn cholesky"
        print("Running command: " + command)
