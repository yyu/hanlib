#!/usr/bin/env python3


import fileinput
from pypinyin import pinyin, lazy_pinyin, Style


if __name__ == '__main__':
    to_skip = '，。[]()'

    for line in fileinput.input():
        line = line.strip()
        for zi in line:
            if zi in to_skip:
                print(zi, end='')
                continue

            yin = lazy_pinyin(zi)
            yin = yin[0] if len(yin) == 1 else '(%s)' % ','.join(yin)

            allyin = pinyin(zi, heteronym=True)
            if len(allyin) == 1 and len(allyin[0]) == 1:
                allyin = '(%s)' % allyin[0][0]
            elif len(allyin) == 1:
                allyin = allyin[0]

            print('%s\033[0;33m%s\033[0;37m%s\033[0m' % (zi, yin, allyin), end='')

        print()
