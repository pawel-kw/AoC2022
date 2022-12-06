import string
from functools import reduce

char_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)


def check_items(line):
    m = len(line) // 2
    try:
        common = set(line[:m]) & set(line[m:])
    except:
        pass
    res = char_list.index(common.pop())+1
    return res

def find_badges(data):
    badges = 0
    for chunk in data:
        res = list(reduce(lambda i, j: i & j, (set(n) for n in chunk)))
        if res is not None:
            badges +=  char_list.index(res.pop())+1
    return badges


with open('input_day03.txt') as f:
    data = [l.strip('\n') for l in f.readlines()]
    # print(sum([check_items(i) for i in data]))
    n = 3
    chunks = [data[i * n:(i + 1) * n] for i in range((len(data) + n - 1) // n )]
    print(find_badges(chunks))



