#!/usr/bin/env python3


import fileinput
from pypinyin import pinyin, lazy_pinyin, Style


if __name__ == '__main__':
    for line in fileinput.input():
        line = line.strip()
        print(' '.join(lazy_pinyin(line)))
        print(line)
        print(' \n')