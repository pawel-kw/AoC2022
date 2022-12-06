from itertools import islice

def find_start(signal):
    window_size = 14
    for i in range(len(signal) - window_size + 1):
        chunk = signal[i: i + window_size]
        if len(chunk) == len(set(chunk)):
            print(f"Found signal at {i+window_size}: {chunk}")
            break

    
with open('input_day06.txt') as f:  
    [signal] = [l.strip('\n') for l in f.readlines()]
    find_start(signal)