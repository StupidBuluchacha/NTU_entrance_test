
# set the depth of recursion
import sys
# 使用线程 设置递归的单位内存大小
import threading
sys.setrecursionlimit(10000000)

flag = False
flag_1 = False
# count = 0
# recursion
def func(s, num, x, y):
    # s: record the route; num: summed number; x and y: coordinate
    global count, flag_1, flag
    # if flag and flag_1:
    #     return
    # if num > 87127231192:
    #     return
    if x == n - 1 and y == m - 1:
        # count += 1
        # print(count)
        num += y + 1
        # if num in [87127231192, 5994891682, 65, 72, 90, 110]:
        #     if num == 87127231192:
        #         flag = True
        #     if num == 5994891682:
        #         flag_1 = True
        #     result[num] = s
        result[num] = s
    elif x == n - 1 and y != m - 1:
        func(s + 'D', num + y + 1, x, y + 1)
    elif x != n - 1 and y == m - 1:
        func(s + 'R', num + y + 1, x + 1, y)
    else:
        func(s + 'D', num + y + 1, x, y + 1)
        func(s + 'R', num + y + 1, x + 1, y)


def main():
    global m, n, result, count
    with open('output_question_1.txt', 'w') as f:
        m = 9
        n = 9
        result = {}
        func('', 0, 0, 0)
        f.write('65' + ' ' + result[65] + '\n')
        f.write('72' + ' ' + result[72] + '\n')
        f.write('90' + ' ' + result[90] + '\n')
        f.write('110' + ' ' + result[110] + '\n')
        f.write('\n')
        print('9,9')
        m = 90000
        n = 100000
        result = {}
        count = 0
        func('', 0, 0, 0)
        f.write('87127231192' + ' ' + result[87127231192] + '\n')
        f.write('5994891682' + ' ' + result[5994891682] + '\n')


# 设置可使用内存大小
threading.stack_size(200000000)
thread = threading.Thread(target=main)
thread.start()
