from __future__ import unicode_literals
import datetime
from os.path import join
import pandas as pd
import sys
import io
from subprocess import check_output


def remove_repeated_spaces(data):
    output = []
    for line in data.split('\n'):
        output.append(' '.join(line.split()))
    return '\n'.join(output)


def process_data(d):
    d = remove_repeated_spaces(d)
    f = io.StringIO(d)
    return pd.read_csv(f, header=0, sep=' ')


def save_snapshot(dst, df):
    now = datetime.datetime.now()
    df.to_feather(join(dst, str(now) + '.feather'))


if __name__ == '__main__':
    output = check_output(['bjobs', '-sum']).decode()

    df = process_data(output)
    save_snapshot(sys.argv[1], df)
