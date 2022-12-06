def build_stacks(input):
    stack_keys = [int(i) for i in input[-1].strip().split('  ')]
    mask = [i.isalpha() for i in input[7]]
    pkg_idx = [i for i, x in enumerate(mask) if x]
    tmp = input[::-1]
    tmp.pop(0)
    stacks = {key: [] for key in stack_keys}
    for i, row in enumerate(tmp):
        data = [row[idx] for idx in pkg_idx]
        for j, key in enumerate(data):
            if key.isalpha():
                stacks[j+1].append(key)
    return stacks

def apply_moves(stacks, moves):
    for i, move in enumerate(moves):
        n, b, e, = [int(item) for item in move.split()[1::2]]
        for j in range(n):
            stacks[e].append(stacks[b].pop())
    return stacks

def apply_moves_2(stacks, moves):
    for i, move in enumerate(moves):
        n, b, e, = [int(item) for item in move.split()[1::2]]
        stacks[e] += stacks[b][-n:]
        del stacks[b][-n:]
    return stacks


with open('input_day05.txt') as f:
    data = [l.strip('\n') for l in f.readlines()]
    n = data.index('')
    stacks_input = data[:n]
    moves_input = data[n+1:]
    stacks = build_stacks(stacks_input)
    moved_stacks = apply_moves_2(stacks, moves_input)
    print(''.join([moved_stacks[key].pop() for key in moved_stacks.keys()]))