class dir_tree:
    def __init__(self):
        self.tree = {'total_size': 0, 'file_size': 0}
        self.current_dir = self.tree
        self.level_up = None
        self.path = []

    def parse_command(self, command: str):
        command = command.split(' ')[1:]
        if command[0] == 'ls':
            # Do nothing - data will be registered by calling self.register_data()
            pass 
        elif command[0] == 'cd':
            if command[1] == '..':
                # Go up
                if self.level_up is not None:
                    self.path.pop()
                    self.current_dir = self.level_up
                    self.level_up = self.find(self.path[:-1])
            elif command[1] == '/':
                self.current_dir = self.tree
                self.path = []
            else:
                self.level_up = self.current_dir
                self.current_dir = self.current_dir.get(command[1])
                self.path.append(command[1])

    def register_data(self, data):
        data = data.split(' ')
        if data[0] == 'dir':
            if data[1] not in self.current_dir.keys():
                self.current_dir[data[1]] = {'total_size': 0, 'file_size': 0}
        else:
            self.current_dir[data[1]] = int(data[0])
            self.current_dir['file_size'] += int(data[0])
            self.add_to_total_size(int(data[0]))

    def find(self, path):
        res = self.tree
        for key in path:
            res = res[key]
        return res

    def add_to_total_size(self, value):
        curr_path = self.tree
        self.current_dir['total_size'] += value
        self.tree['total_size'] += value
        for key in self.path[:-1]:
            curr_path = curr_path[key]
            curr_path['total_size'] += value

    def find_sum_size(self,level):
        def iter_paths(d):
            r = 0
            for k,v in d.items():
                if isinstance(v,dict):
                    r += iter_paths(v)
                elif (k == 'total_size') & (v <= level):
                    r += v
            return r
        return iter_paths(self.tree)
    
    def find_dir_larger_than(self, level):
        def iter_paths(d):
            r = []
            for k,v in d.items():
                if isinstance(v,dict):
                    r += iter_paths(v)
                elif (k == 'total_size') & (v >= level):
                    r.append(v)
            return r
        return min(iter_paths(self.tree))

with open('input_day07.txt') as f:  
    data = [l.strip('\n') for l in f.readlines()]
    my_tree = dir_tree()
    for i, line in enumerate(data):
        if line[0] == "$":
            my_tree.parse_command(line)
        else:
            my_tree.register_data(line)

print(f"Total size taken: {my_tree.tree['total_size']}")
print(f"Total size of directories larger than 100000: {my_tree.find_sum_size(100000)}")
total_size = 70000000
needed = 30000000
remaining = total_size - my_tree.tree['total_size']
goal = needed - remaining
print(f"Remaining disc space: {remaining}")
print(f"Need to free up {goal}")
print(f"Smallest directory big enough: {my_tree.find_dir_larger_than(goal)}")
    