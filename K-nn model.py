import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('knn_base.csv', encoding="utf-8")
data_z = np.array(data['분류대상'])

datab_xy = data[["당도", "아삭함"]]
data_xy = datab_xy.values

sugar = int(input('당도를 입력하세요 (1 ~ 10) : '))
chew = int(input('아삭함의 정도를 입력하세요 (1 ~ 10) : '))
target = [sugar, chew]


def data_set():
    size = len(datab_xy)
    class_target = np.tile(target, (size, 1))
    class_z = np.array(data_z)
    return datab_xy, class_target, class_z


dataset, class_target, class_z = data_set()


def classify(dataset, class_target, class_category, k):
    diffMat = class_target - dataset
    spdiffMat = diffMat ** 2
    row_sum = spdiffMat.sum(axis=1)
    distance = np.sqrt(row_sum)
    sortDist = distance.argsort()

    class_result = {}
    for i in range(k):
        c = class_category[sortDist[i]]
        class_result[c] = class_result.get(c, 0) + 1

    return class_result


def result_print(class_result):
    fruit = vege = 0
    for c in class_result.keys():
        if c == '과일':
            fruit = class_result[c]
        elif c == '채소':
            vege = class_result[c]

    if fruit > vege:
        result = "분류한 대상은 과일입니다."
    elif vege > fruit:
        result = "분류한 대상은 채소입니다."
    else:
        result = "K값을 변경해서 다시 시도해주세요."

    return result


k = int(input('k값을 입력해주세요 : '))
class_result = classify(data_xy, class_target, class_z, k)
print(class_result)
print(result_print(class_result))


for c in range(len(datab_xy)):
    if data_z[c] == '과일':
        plt.scatter(data_xy[c][0], data_xy[c][1], marker='o', color='b')
    elif data_z[c] == '채소':
        plt.scatter(data_xy[c][0], data_xy[c][1], marker='+', color='g')

plt.scatter(sugar, chew, marker='x', color='gray')
plt.show()
