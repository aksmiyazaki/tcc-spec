import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from colour import Color
import palettable

%matplotlib inline

csv_input = "/home/aksmiyazaki/git/tcc-spec/experiments/results/extracted_results.csv"

df = pd.read_csv("/home/aksmiyazaki/git/tcc-spec/experiments/results/extracted_results.csv", header=0)
df = df.replace("seq", "Sequencial")
df = df.replace("d1node", "1 Nó")
df = df.replace("d2node", "2 Nós")
df = df.replace("d3node", "3 Nós")
df.head()

sns.set(style="whitegrid")
sns.set(rc={'figure.figsize':(15,10)})


def common_barplot(df, font_sz, title, save_path = ''):
    N = len(df['Exec'].unique())
    ind = np.arange(N)
    width = 0.5
    current_palette = palettable.colorbrewer.qualitative.Set1_9.mpl_colors

    f = plt.figure()
    piv_df = df.pivot(index="Id", columns="Exec", values=["Total"])

    dataset1 = piv_df['Total'][['Sequencial', '1 Nó', '2 Nós', '3 Nós']].mean().to_numpy()
    dataset1_err = piv_df['Total'][['Sequencial', '1 Nó', '2 Nós', '3 Nós']].std().to_numpy()

    dataset1_err[0] = 3 * (dataset1_err[0]/len(piv_df['Total']['Sequencial'].dropna()))
    dataset1_err[1] =3 * (dataset1_err[1]/len(piv_df['Total']['1 Nó'].dropna()))
    dataset1_err[2] =3 * (dataset1_err[2]/len(piv_df['Total']['2 Nós'].dropna()))
    dataset1_err[3] =3 * (dataset1_err[3]/len(piv_df['Total']['3 Nós'].dropna()))

    p1 = plt.bar(ind, dataset1, width, yerr=dataset1_err, color=current_palette[0], error_kw={'capsize':20, 'ecolor':'black'})

    p1[1].set_color(current_palette[1])
    p1[2].set_color(current_palette[2])
    p1[3].set_color(current_palette[3])

    plt.ylim([0,1601])
    plt.yticks(fontsize=font_sz)
    plt.ylabel("Tempo (S)", fontsize=font_sz)
    plt.xticks(ind, ['1', '15', '15+15', '15+15+15'], fontsize=font_sz)
    plt.xlabel('Nível de Paralelismo', fontsize=font_sz)
    plt.gca().xaxis.grid(False)
    plt.title(title, fontsize=font_sz)
    if len(save_path) > 0:
        f.savefig(save_path, bbox_inches='tight')
    plt.show()

def stacked_barplot(df, font_sz, title, save_path = '', colarr=['Sequencial','1 Nó', '2 Nós', '3 Nós'], idxarr=['1', '15', '15+15', '15+15+15'], maxv = 1601):
    N = len(colarr)
    ind = np.arange(N)
    width = 0.5
    current_palette = palettable.colorbrewer.qualitative.Set1_9.mpl_colors
    f = plt.figure()

    piv_df = df.pivot(index="Id", columns="Exec", values=["State", "Variable", "Link","DAG","Entities","Events","GAPS","Write"])

    dataset1 = piv_df['State'][colarr].mean().to_numpy()
    dataset2 = piv_df['Variable'][colarr].mean().to_numpy()
    dataset3 = piv_df['Link'][colarr].mean().to_numpy()
    dataset4 = piv_df['DAG'][colarr].mean().to_numpy()
    dataset5 = piv_df['Entities'][colarr].mean().to_numpy()
    dataset6 = piv_df['Events'][colarr].mean().to_numpy()
    dataset7 = piv_df['GAPS'][colarr].mean().to_numpy()
    dataset8 = piv_df['Write'][colarr].mean().to_numpy()

    p1 = plt.bar(ind, dataset1, width, color=current_palette[0])
    p2 = plt.bar(ind, dataset2, width, bottom=dataset1, color=current_palette[1])
    p3 = plt.bar(ind, dataset3, width, bottom =[sum(x) for x in zip(dataset1,dataset2)], color=current_palette[2])
    p4 = plt.bar(ind, dataset4, width, bottom =[sum(x) for x in zip(dataset1,dataset2,dataset3)], color=current_palette[3])
    p5 = plt.bar(ind, dataset5, width, bottom =[sum(x) for x in zip(dataset1,dataset2,dataset3,dataset4)], color=current_palette[4])
    p6 = plt.bar(ind, dataset6, width, bottom =[sum(x) for x in zip(dataset1,dataset2,dataset3,dataset4,dataset5)], color=current_palette[5])
    p7 = plt.bar(ind, dataset7, width, bottom =[sum(x) for x in zip(dataset1,dataset2,dataset3,dataset4,dataset5,dataset6)], color=current_palette[6])
    p8 = plt.bar(ind, dataset8, width, bottom =[sum(x) for x in zip(dataset1,dataset2,dataset3,dataset4,dataset5,dataset6,dataset7)], color=current_palette[7])

    plt.ylim([0,maxv])
    plt.yticks(fontsize=font_sz)
    plt.ylabel("Tempo (S)", fontsize=font_sz)
    plt.xticks(ind, idxarr, fontsize=font_sz)
    plt.xlabel('Nível de Paralelismo', fontsize=font_sz)
    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0]), ('State', 'Variable', 'Link', 'DAG', 'Entities', 'Events', 'GAPS', 'Write'), fontsize=font_sz, ncol=2, framealpha=0, fancybox=True)
    plt.gca().xaxis.grid(False)
    plt.title(title, fontsize=font_sz)
    if len(save_path) > 0:
        f.savefig(save_path, bbox_inches='tight')
    plt.show()

common_barplot(df, 22, 'Tempo total', '/home/aksmiyazaki/git/tcc-spec/experiments/total.pdf')
stacked_barplot(df, 22, 'Tempo total por etapa', '/home/aksmiyazaki/git/tcc-spec/experiments/total_step.pdf')
#stacked_barplot_normalized(df, 22, 'Tempo relativo entre execuções', '/home/aksmiyazaki/git/tcc-spec/experiments/total_relative.pdf')
#def stacked_barplot_normalized(df, font_sz, title, save_path = ''):
#    N = len(df['Exec'].unique())
#    ind = np.arange(N)
#    width = 0.5
#    current_palette = palettable.colorbrewer.qualitative.Set1_9.mpl_colors
#    f = plt.figure()
#
#    piv_df = df.pivot(index="Id", columns="Exec", values=["State", "Variable", "Link","DAG","Entities","Events","GAPS","Write"])
#    total_sequential = df[df['Exec'] == 'Sequencial'][["State", "Variable", "Link","DAG","Entities","Events","GAPS","Write"]].mean().sum()
#    total_2n = df[df['Exec'] == '2 Nós'][["State", "Variable", "Link","DAG","Entities","Events","GAPS","Write"]].mean().sum()
#    total_3n = df[df['Exec'] == '3 Nós'][["State", "Variable", "Link","DAG","Entities","Events","GAPS","Write"]].mean().sum()
#
#    arr_total = np.array([total_sequential, total_2n, total_3n])
#
#    dataset1 = (piv_df['State'][['Sequencial', '2 Nós', '3 Nós']].mean().to_numpy() / arr_total) * 100
#    dataset2 = (piv_df['Variable'][['Sequencial', '2 Nós', '3 Nós']].mean().to_numpy() / arr_total) * 100
#    dataset3 = (piv_df['Link'][['Sequencial', '2 Nós', '3 Nós']].mean().to_numpy() / arr_total) * 100
#    dataset4 = (piv_df['DAG'][['Sequencial', '2 Nós', '3 Nós']].mean().to_numpy() / arr_total) * 100
#    dataset5 = (piv_df['Entities'][['Sequencial', '2 Nós', '3 Nós']].mean().to_numpy() / arr_total) * 100
#    dataset6 = (piv_df['Events'][['Sequencial', '2 Nós', '3 Nós']].mean().to_numpy() / arr_total) * 100
#    dataset7 = (piv_df['GAPS'][['Sequencial', '2 Nós', '3 Nós']].mean().to_numpy() / arr_total) * 100
#    dataset8 = (piv_df['Write'][['Sequencial', '2 Nós', '3 Nós']].mean().to_numpy() / arr_total) * 100
#
#    p1 = plt.bar(ind, dataset1, width, color=current_palette[0])
#    p2 = plt.bar(ind, dataset2, width, bottom=dataset1, color=current_palette[1])
#    p3 = plt.bar(ind, dataset3, width, bottom =[sum(x) for x in zip(dataset1,dataset2)], color=current_palette[2])
#    p4 = plt.bar(ind, dataset4, width, bottom =[sum(x) for x in zip(dataset1,dataset2,dataset3)], color=current_palette[3])
#    p5 = plt.bar(ind, dataset5, width, bottom =[sum(x) for x in zip(dataset1,dataset2,dataset3,dataset4)], color=current_palette[4])
#    p6 = plt.bar(ind, dataset6, width, bottom =[sum(x) for x in zip(dataset1,dataset2,dataset3,dataset4,dataset5)], color=current_palette[5])
#    p7 = plt.bar(ind, dataset7, width, bottom =[sum(x) for x in zip(dataset1,dataset2,dataset3,dataset4,dataset5,dataset6)], color=current_palette[6])
#    p8 = plt.bar(ind, dataset8, width, bottom =[sum(x) for x in zip(dataset1,dataset2,dataset3,dataset4,dataset5,dataset6,dataset7)], color=current_palette[7])
#
#    plt.ylim([0,120])
#    plt.yticks(fontsize=font_sz)
#    plt.ylabel("Tempo em %", fontsize=font_sz)
#    plt.xticks(ind, ['1', '16+16', '15+15+15'], fontsize=font_sz)
#    plt.xlabel('Nível de Paralelismo', fontsize=font_sz)
#    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0]), ('State', 'Variable', 'Link', 'DAG', 'Entities', 'Events', 'GAPS', 'Write'), fontsize=font_sz, ncol=4, framealpha=0, fancybox=True)
#    plt.gca().xaxis.grid(False)
#    plt.title(title, fontsize=22)
#    if len(save_path) > 0:
#        f.savefig(save_path, bbox_inches='tight')
#    plt.show()
