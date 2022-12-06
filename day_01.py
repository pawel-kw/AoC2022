input_data_file = "./input_data.txt"

# read in the data
with open(input_data_file) as f:
    input_data = f.readlines()

food_list = {}
reindeer_counter = 1
for item in input_data:
    item = item.strip('\n')
    if item != '':
        item = int(item)
        if reindeer_counter not in food_list.keys():
            food_list[reindeer_counter] = {'items': [item], 'sum': item}
        else:
            food_list[reindeer_counter]['items'].append(item)
            food_list[reindeer_counter]['sum'] += item
    else:
        reindeer_counter += 1
max_cals = print(max(d['sum'] for d in food_list.values()))
sorted_cals = sorted(d['sum'] for d in food_list.values())
print(sorted_cals[-3:])
print(sum(sorted_cals[-3:]))