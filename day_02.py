points = {'X': 1, 'Y': 2, 'Z': 3}
pairs = {'A': 'Y', 'B': 'Z', 'C': 'X'}
dictionary = {'A': 'X', 'B': 'Y', 'C': 'Z'}

def eval_round(data):
    res = 0
    player1, player2 = [d.strip('\n') for d in data.split(' ')]
    # Check if win:
    if pairs[player1] == player2:
        # We have a win
        res = points[player2] + 6
    elif dictionary[player1] == player2:
        # draw
        res = points[player2] + 3
    else:
        # lost
        res = points[player2]
    return res

info = {
    'A': 1,
    'B': 2,
    'C': 3,
}

win_pair = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

loose_pair = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

points2 = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

def eval_round_2(data):
    player1, player2 = [d.strip('\n') for d in data.split(' ')]
    # win case
    if player2 == 'Z':
        res = 6 + info[win_pair[player1]]
    # draw case
    elif player2 =='Y':
        res = 3 + info[player1]
    # loose case
    else:
        res = info[loose_pair[player1]]
    return res
    

score = 0
with open('input_day02.txt') as f:
    data = f.readlines()

for round in data:
    score += eval_round_2(round)

print(score)
