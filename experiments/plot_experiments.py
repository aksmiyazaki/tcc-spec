import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

csv_input = "/home/aksmiyazaki/git/tcc-spec/experiments/results/extracted_results.csv"

df = pd.read_csv("/home/aksmiyazaki/git/tcc-spec/experiments/results/extracted_results.csv", header=0)
df.head()

df = df.replace("seq", "Sequencial")
df = df.replace("d2node", "2 Nós")
df = df.replace("d3node", "3 Nós")
df.head()


sns.set(style="whitegrid")
sns.set(rc={'figure.figsize':(15,15)})
ax = sns.barplot(x="Exec", y="Total", data=df).set(xlabel='Tipo de Execução', ylabel='Tempo (s)', title='Tempo Total')
