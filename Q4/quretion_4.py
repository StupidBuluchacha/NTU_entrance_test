# for data copy
import copy
# open input file
with open('input_question_4') as file:
    # deal with data of input file
    data = [[int(j) for j in i.split('\t') if j] for i in file.read().split('\n') if i]
    # number of cluster
    num = 1
    # 4-connectivity or 8-connectivity?
    flag = 8
    # store data coordinate in the list
    data_1 = []
    # add coordinate to the list
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]:
                data_1.append((i, j))
    # 4-connectivity
    if flag == 4:
        # temporary data list
        data_2 = []
        # calculate cluster coordinate
        while data_1:
            d = [data_1.pop()]
            # deal with coordinate in same cluster
            while True:
                for i in d:
                    if (i[0] + 1, i[1]) in data_1:
                        data_1.remove((i[0] + 1, i[1]))
                        d.append((i[0] + 1, i[1]))
                    if (i[0] - 1, i[1]) in data_1:
                        data_1.remove((i[0] - 1, i[1]))
                        d.append((i[0] - 1, i[1]))
                    if (i[0], i[1] + 1) in data_1:
                        data_1.remove((i[0], i[1] + 1))
                        d.append((i[0], i[1] + 1))
                    if (i[0], i[1] - 1) in data_1:
                        data_1.remove((i[0], i[1] - 1))
                        d.append((i[0], i[1] - 1))
                if (i[0] + 1, i[1]) not in data_1 or (i[0] - 1, i[1]) not in data_1\
                        or (i[0], i[1] + 1) not in data_1 or (i[0], i[1] - 1) not in data_1:
                    break
            data_2.append(d)
        # print(data_2)
        # convert numbers in same cluster into same numbers
        res = copy.copy(data)
        for i in data_2:
            for j in i:
                res[j[0]][j[1]] = num
            num += 1
        # print(res)
    # 8-connectivity
    elif flag == 8:
        data_2 = []
        while data_1:
            d = [data_1.pop()]
            while True:
                for i in d:
                    if (i[0] + 1, i[1]) in data_1:
                        data_1.remove((i[0] + 1, i[1]))
                        d.append((i[0] + 1, i[1]))
                    if (i[0] - 1, i[1]) in data_1:
                        data_1.remove((i[0] - 1, i[1]))
                        d.append((i[0] - 1, i[1]))
                    if (i[0], i[1] + 1) in data_1:
                        data_1.remove((i[0], i[1] + 1))
                        d.append((i[0], i[1] + 1))
                    if (i[0], i[1] - 1) in data_1:
                        data_1.remove((i[0], i[1] - 1))
                        d.append((i[0], i[1] - 1))
                    if (i[0] + 1, i[1] + 1) in data_1:
                        data_1.remove((i[0] + 1, i[1] + 1))
                        d.append((i[0] + 1, i[1] + 1))
                    if (i[0] - 1, i[1] + 1) in data_1:
                        data_1.remove((i[0] - 1, i[1] + 1))
                        d.append((i[0] - 1, i[1] + 1))
                    if (i[0] - 1, i[1] + 1) in data_1:
                        data_1.remove((i[0] - 1, i[1] + 1))
                        d.append((i[0] - 1, i[1] + 1))
                    if (i[0] - 1, i[1] - 1) in data_1:
                        data_1.remove((i[0] - 1, i[1] - 1))
                        d.append((i[0] - 1, i[1] - 1))
                if (i[0] + 1, i[1]) not in data_1 or (i[0] - 1, i[1]) not in data_1 \
                        or (i[0], i[1] + 1) not in data_1 or (i[0], i[1] - 1) not in data_1 \
                        or (i[0] + 1, i[1] + 1) not in data_1 or (i[0] - 1, i[1] + 1) not in data_1 \
                        or (i[0] - 1, i[1] + 1) not in data_1 or (i[0] + 1, i[1] - 1) not in data_1:
                    break
            data_2.append(d)
        # print(data_2)
        res = copy.copy(data)
        for i in data_2:
            for j in i:
                res[j[0]][j[1]] = num
            num += 1

# data storage
with open('output_question_4.txt', 'w') as f:
    for i in res:
        f.write(' '.join([str(j) for j in i]) + '\n')