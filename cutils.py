import numpy as np 
import matplotlib.pyplot as plt 

nrows = 100000

def plot_pie(x, nrows):
    values = x.value_counts().values
    labels = x.value_counts().index
    explode = [0] * len(labels)
    explode[np.argmax(values)] = .1
    _,_, apct = plt.pie(values, labels = labels, explode = explode, autopct = '%1.1f%%')
    for a in apct:
        a.set_color('black')

def get_rows(n, col):
    if n % col == 0:
        return n // col
    return (n // col) + 1

def group_pie_plot(df, groupby, x, n, c = 5, total_rows = nrows):
    r = get_rows(n, c)
    plt.tight_layout()
    iterr = 1
    for row, rdf in df.groupby(groupby):
        plt.subplot(r, c, iterr)
        plt.title(row)
        plot_pie(rdf[x], rdf.shape[0])
        iterr += 1