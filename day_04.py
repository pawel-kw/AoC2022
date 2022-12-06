def gen_range(pair):
    return [x for x in range(pair[0], pair[1] + 1)]

def test_sets(data):
    res = 0
    overlap = 0
    for line in data:
        pairs = [[int(i) for i in item.split("-")] for item in line.split(",")]
        sets = [gen_range(pair) for pair in pairs]
        if set(sets[0]).issubset(sets[1]) or set(sets[1]).issubset(sets[0]):
            res += 1
        if set(sets[0]) & set(sets[1]):
            overlap += 1
    return [res, overlap]


with open('input_day04.txt') as f:
    data = [l.strip('\n') for l in f.readlines()]
    print(test_sets(data))
