import pandas as pd
import os
import re
import glob
import seaborn as sns

aimdir = {'seq':'/home/aksmiyazaki/git/tcc-spec/experiments/results/experiment_seq/',
    'd1node':'/home/aksmiyazaki/git/tcc-spec/experiments/results/experiment_distrib_1node/',
    'd2node':'/home/aksmiyazaki/git/tcc-spec/experiments/results/experiment_distrib/',
    'd3node': '/home/aksmiyazaki/git/tcc-spec/experiments/results/experiment_distrib_3nodes/'}

def convert_regex_match(regex_group):
    return float(str(match.group(1))[:-1])


df = pd.DataFrame(columns=['Id', 'Exec', 'State','Variable','Link','DAG','Entities','Events', 'GAPS', 'Parsing', 'Write', 'Total'])

for key, value in aimdir.items():
    file_names = [f for f in glob.glob(value + 'experiment_[0-9][0-9].log')]
    file_names.sort()
    exp_iter = 0

    for fname in file_names:
        if fname == '':
            break

        state_time = -1
        variable_time = -1
        link_time = -1
        DAG_time = -1
        entities_time = -1
        events_time = -1
        gaps_time = -1
        parsing_time = -1
        write_time = -1
        total_time = -1

        with open(fname, 'r') as logfile:
            print("Parsing [" + fname + "]")
            for line in logfile:
                match = re.match(r'.*State CSV took {(.*)}', line)
                if match and state_time == -1:
                    state_time = convert_regex_match(match)
                    continue
                elif match and state_time != -1:
                    events_time = convert_regex_match(match)
                    continue

                match = re.match(r'.*Variable CSV took {(.*)}', line)
                if match:
                    variable_time = convert_regex_match(match)
                    continue

                match = re.match(r'.*Link CSV took {(.*)}', line)
                if match:
                    link_time = convert_regex_match(match)
                    continue

                match = re.match(r'.*DAG CSV took {(.*)}', line)
                if match:
                    DAG_time = convert_regex_match(match)
                    continue

                match = re.match(r'.*Entities\/Y CSV took {(.*)}', line)
                if match:
                    entities_time = convert_regex_match(match)
                    continue

                match = re.match(r'.*Events CSV took {(.*)}', line)
                if match:
                    events_time = convert_regex_match(match)
                    continue

                match = re.match(r'.*Gaps Calculation took {(.*)}', line)
                if match:
                    gaps_time = convert_regex_match(match)
                    continue

                match = re.match(r'.*Reading and parsing all files took {(.*)}', line)
                if match:
                    parsing_time = convert_regex_match(match)
                    continue

                match = re.match(r'.*Writing all files took {(.*)}', line)
                if match:
                    write_time = convert_regex_match(match)
                    continue

                match = re.match(r'.*Entire Execution took {(.*)}', line)
                if match:
                    total_time = convert_regex_match(match)
                    continue
            if state_time > -1 and variable_time > -1 and gaps_time > -1:
                df.loc[len(df)] = [int(exp_iter), key, state_time, variable_time, link_time, DAG_time,
                                        entities_time, events_time, gaps_time, parsing_time,
                                    write_time, total_time]
                exp_iter += 1
            else:
                print("Result from file [" + fname + "] Is corrupted");
df.head()
df = df.set_index('Id')

df.to_csv(path_or_buf='/home/aksmiyazaki/git/tcc-spec/experiments/results/extracted_results.csv',
            header=True)

sns.set(style="whitegrid")
sns.set(rc={'figure.figsize':(15,15)})
sns_plot = sns.barplot(x="Exec", y="Total", data=df)
fig = sns_plot.get_figure()
fig.savefig("/home/aksmiyazaki/git/tcc-spec/experiments/output.png")
