import os
from os.path import join
import pandas as pd
import sys
from dateutil.parser import parse as date_parse

import matplotlib.pyplot as plt, mpld3


def process_reports(dst):
    files = []
    for fn in os.listdir(dst):
        date = date_parse(fn.replace('.feather', ''))
        files.append((date, fn))
    files = sorted(files, key=lambda x: x[0])

    dfs = []
    for f in files:
        df = pd.read_feather(join(dst, f[1]))
        df['date'] = f[0]
        df = df.set_index('date')
        dfs.append(df)
    df = pd.concat(dfs, axis=0)
    df.plot(subplots=True)
    mpld3.save_html(plt.gcf(), "index.html")


if __name__ == '__main__':
    process_reports(sys.argv[1])
