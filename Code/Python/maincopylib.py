import numpy as np 
import copy


# n - количество регистров, m - шаг регистров(на каком x[i] будет использоваться регистр stack)
#n, m = 4, 5
def ConvolutionalInterleaver(n, m, l):

    def myround(number):
        if number%1 == 0:
            number = int(number)
        else:
            number = int(number)+1
        return number

    assert n > 0
    assert m > 0
    assert l > 0

    x = [i for i in range(1, l+1)]
    tt = myround(len(x)/n)
    x = [x[n*i:(i + 1)*n] for i in range(tt)] # Переход коммутатора на регистры
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

    def shift(all_y, n, m, l):
        s = []
        ind = 0
        #N = l//n//m
        N=l/n/m
        if N < 1:
            return all_y[0]
        N=myround(N)
        for j in range(N):
            for i in [k for k in range(m)]: #поочередно беру массивы
                yk = all_y[i]

                ind = j*m
                if len(yk) > ind: 
                    s.append(yk[ind])
            #ind += m
        return s




    all_y = []
    all_s = []
    #N = n//m 
    N = myround(l/n)
    if N < 1:
        N = 1
    
    for j in range(1, N+1):
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
        ans = shift(all_y, n, m, l)
    else:
        ans = all_y
    
    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    output = ','.join(map(str, flatten(ans)))
    return output
#print(ans)

ConvolutionalInterleaver(2, 2, 8)
#ConvolutionalInterleaver(2, 2, 12)
#ConvolutionalInterleaver(2, 2, 10)
#ConvolutionalInterleaver(4, 5, 16)
#ConvolutionalInterleaver(4, 5, 17)


def decode(n, m, l):

    def shiD(i, D, n):
        B = i//n+1 # В каком блоке я нахожусь?

        Bn = i%n+1 # Какой элемент блока по счету сейчас?

        dn = D - (i % n) * n # Расчет на сколько я сдвигаю элемент блока...
        #T = 2**n


        if Bn == n:
            dn = 0

        return dn

    def funcBuf(l, D, i):
        point = l - D - i # 0 или меньше 0 - не входит в диапазон
        return point

    assert n > 0
    assert m > 0
    assert l > 0

    x = ConvolutionalInterleaver(n, m, l)

    x = x.split(',')
    x = [int(i) for i in x]

    D = n*(n-1)*m # сдвиг (задержка) нужен для правильного декодирования
    
    # с тем как рассчитывается шаг не уверен, в статьях не нашел нужного
    d = [shiD(i, D, n) for i in range(0, len(x))]
    pos = [a for a in range(0, len(x))]
    y = [0 for a in range(0, len(x))] # заготовка для перестановок

    if funcBuf(len(x), d[0], 0) > 0:
        y[pos[0] + d[0]] = x[0]
    # Перестановки делаю
    for i in range(n, len(x)):
        ind = pos[i] + d[i]

        if funcBuf(len(x), d[i], i) > 0:
            y[ind] = x[i]

    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    output = ','.join(map(str, flatten(y)))

    return output

#decode(2, 1, 8) # +++
#decode(3, 1, 9) # +++
#decode(2, 1, 20) # +++
#decode(3, 1, 18)
#decode(4, 1, 20)
#decode(7, 1, 20)

#decode(2, 2, 8)
decode(2, 2, 16)


