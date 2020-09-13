import pandas as pd

line_counter = 0
header = []
base_list = []

# data = pd.read_csv('./knn_base.csv', encoding='utf-8')
# print(data['분류대상'])
with open('knn_base.csv', encoding='utf-8') as f:
    while 1:
        data = f.readline()
        if not data:
            break
        if line_counter == 0:
            header = data.split(",")
        else:
            base_list.append(data.split(","))
        line_counter += 1

print(header, base_list)
