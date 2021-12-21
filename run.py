# coding:utf8
import json
import random


def main():
    result_big = set()
    result_mid = set()
    result_small = set()
    big_count = 4
    mid_count = 4
    small_count = 4
    with open('./menu.json', 'r', encoding='UTF-8') as infile:
        j = json.load(infile)
        big = list(j['big'].keys())
        for i in range(1, 100):
            random.shuffle(big)

        mid = list(j['mid'].keys())
        for i in range(1, 100):
            random.shuffle(mid)

        small = list(j['small'].keys())
        for i in range(1, 100):
            random.shuffle(small)

        while len(result_big) < big_count:
            x = random.choices(big)[0]
            result_big.add(x)
        while len(result_mid) < mid_count:
            x = random.choices(mid)[0]
            result_mid.add(x)
        while len(result_small) < small_count:
            x = random.choices(small)[0]
            result_small.add(x)

        print('==大菜==')
        for b in result_big:
            print('{}'.format(b))
            print('{}'.format(j['big'][b]['material']))
            print('')

        print('')
        print('')
        print('==中菜==')
        print('')
        print('')
        for m in result_mid:
            print('{}'.format(m))
            print('{}'.format(j['mid'][m]['material']))
            print('')
        print('')
        print('')
        print('==小菜==')
        for s in result_small:
            print('{}'.format(s))
            print('{}'.format(j['small'][s]['material']))
            print('')

    pass


if __name__ == '__main__':
    main()
