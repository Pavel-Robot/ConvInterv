include("code.jl") # сверточное перемежение
include("decode_func.jl") # Функции для этого блока


# Реализация блока сверточного перемежения (основная функция декодирования)
# x - входной вектор (состоит из целых чисел уже прошедших кодирование)
# n - количество регистров, m - шаг
# регистров(на каком x[i] будет использоваться регистр)
#function ConvolutionalInterleaver(x::Vector, n::Int64, m::Int64, l::Int64)
function decode(x::Vector, n::Int64, m::Int64)

    l = length(x)
    D = n*(n-1)*m # сдвиг (задержка) нужен для правильного декодирования
    
    # с тем как рассчитывается шаг не уверен, в статьях не нашел нужного
    # для всех тестов верно считает, как в матлабе, но есть случаи, когда и не верно
    d = [stepD(i, D, n) for i=0:l-1] # сдвиг для каждого элемента
    pos = [a for a=1:l] # позиции
    y = [0 for num=1:l] # заготовка для перестановок

    # Перестановки делаю
    for i=1:l
        ind = pos[i] + d[i]

        if funcBuf(l, d[i], i) >= 0
            y[ind] = x[i]
        end
    end

    #text = join(vcat(y...), ",")
    #return text
    return y
end

#=
size = 16
x = collect(1:size)
encoding = ConvolutionalInterleaver(x, 2, 2)
decoding = decode(encoding, 2, 2)
println(decoding)
=#