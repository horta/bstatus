import datetime
from os.path import join
import pandas as pd
import sys
import io


def remove_repeated_spaces(data):
    output = []
    for line in data.split('\n'):
        output.append(' '.join(line.split()))
    return '\n'.join(output)


def process_file(fp):
    d = open(fp).read()
    d = remove_repeated_spaces(d)
    f = io.StringIO(d)
    return pd.read_csv(f, header=0, sep=' ')


def save_snapshot(dst, df):
    now = datetime.datetime.now()
    df.to_feather(join(dst, str(now) + '.feather'))


if __name__ == '__main__':
    df = process_file(sys.argv[1])
    save_snapshot(sys.argv[2], df)
