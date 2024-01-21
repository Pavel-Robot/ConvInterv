import numpy as np 
import copy


# n - количество регистров, m - шаг регистров(на каком x[i] будет использоваться регистр stack)
n, m = 4, 5

class reg:
    def __init__(self, size, number):
        self.size = size
        self.num = number
        if size == 0:
            self.stack = [0] * size
        else:
            self.stack = []


x = [i for i in range(1, 16+1)]
x = [x[n*i:(i + 1)*n] for i in range(len(x)//n)] # Переход коммутатора на регистры
#regs = [reg(i, i+1) for i in range(m+1)] # регистры перехода



def registry_one(x):
    stack_main = []
    output_x = []
    for i in range(len(x)):
        stack = []
        if i == 0:
            output_x.append(x[i])
            stack_main.append(stack)
        else:
            stack = [0] * i
            val = stack.pop(0)
            output_x.append(val)
            stack.append(x[i])
            stack_main.append(stack)

    return output_x, stack_main

def registry_two(x, stack, index, m):
    output_x = []

    if index % m == 0: # то мы попали в блок регистров где будем добавлять и вытаскивать из стека
        for i in range(len(x)):
            if i == 0:
                output_x.append(x[i])
                #stack[i].append(nothing)
            else:
                val = stack[i].pop(0)
                output_x.append(val)
                stack[i].append(x[i])
    else: # не попали, то зануляем все регистры кроме нулевого (или первого)
        for i in range(len(x)):
            if i == 0:
                output_x.append(x[i])
            else:
                output_x.append(0)

    index+=1
    return output_x, stack, index

import numpy as np

def shift(all_y, m):
    s = []
    ind = 0
    for j in range(len(all_y)):
        for i in [k for k in range(m)]: #поочередно беру массивы
            yk = all_y[i]

            ind = j*m
            s.append(yk[ind])
    return s




all_y = []
all_s = []
N = len(x[0])//m + 1
if N < 1:
    N = 1

for j in range(1, N):
    x_out_first, st_first = registry_one(x[j-1])

    y = [x_out_first]
    s = [copy.deepcopy(st_first)]

    index = 1 
    for i in range(j, len(x)):
        x_out, st, index = registry_two(x[i], s[-1], index, m)
        y.append(x_out)
        s.append(copy.deepcopy(st))

    all_y.append(y)
    #all_y.append([[0]*len(x)]*(j-1)+ y)
    
    all_s.append(s)
    #index+=1

if len(all_y) != 1:
    ans = shift(all_y, m)
else:
    ans = all_y

print(ans)