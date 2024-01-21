### Use library ###
#using DataStructures
#include("dequemy.jl"); # Определение очереди
### End use library ###


# Функция округления чисел. Если хотя бы number = 2.1, то на выходе получим 3
# Если 1.5, то получим 2, как и при 1.2->2
function myround(number::Float64)
        if number%1 == 0
            number = floor(Int64, number);
        else
            number = floor(Int64, number) + 1;
        end
        return number
end

# функция делит входной вектор на chunk_count частей, 
# а части размера n (с учетом, что последний chunk может быть меньше n )
function division_x(x::Vector, chunk_count::Int64, n::Int64)
    arr = []
    for i=1:chunk_count
        start_index = (i-1) * n + 1;
        end_index = i * n;

        # Проверяем, если это последняя часть и она должна быть больше
        # Условие 2, если мы в последнем блоке выйдем за размер вектора || start_index + n > length(x)
        if i == chunk_count 
            end_index = length(x);
        end

        # Используем индексацию, чтобы выбрать нужную часть
        elements = x[start_index:end_index];

        push!(arr, elements)
    end

    return arr
    
end

# Функция инициализирует очередь с принципом FIFO для треугольника регистров
# Возвращает кодированный первый вектор и регистры для него со значениями
function registry_one(x::Vector)
    deque_main =[]
    output_x = []
    for i=1:length(x)
        deque = []
        if i == 1
            push!(output_x, x[i])
            push!(deque_main, deque)
        else
            deque = [0 for k=1:i-1]
            value = popfirst!(deque)
            push!(output_x, value)
            push!(deque, x[i])
            push!(deque_main, deque)
        end
    end
    return output_x, deque_main
end

# Функция принимает шаг m, часть вектора x, и значения регистров этого блока, чтобы рассчитать
# следующий блок
function registry_two(x::Vector, reg::Vector, index::Int64, m::Int64)
    output_x = []
    lenx = length(x)

    if index % m == 0   # то мы попали в блок регистров где будем добавлять и вытаскивать из очереди
        for i=1:lenx
            if i == 1
                push!(output_x, x[i])
                #push!(reg[i], nothing)
            else
                value = popfirst!(reg[i])
                push!(output_x, value)
                push!(reg[i], x[i])
            end
        end
    else   # не попали, то зануляем все регистры кроме нулевого (или первого)
        for i=1:lenx
            if i == 1
                push!(output_x, x[i])
            else
                push!(output_x, 0)
            end
        end
    end
    index += 1

    return output_x, reg, index

end

# Функция реализует сдвиги на шаг m при размере блока n и длине входного вектора l
# организует сдвиги векторов all_y
function shift(all_y::Vector, n::Int64, m::Int64, l::Int64)
        array = []
        index = 1
        
        N=l/n/m; if N < 1 return all_y[1] end
        N = myround(l/n/m)
        for j=1:N+1
            for i=1:m #поочередно беру массивы
                yk = all_y[i]

                index = (j-1)*m+1
                if length(yk) > index-1
                    push!(array, yk[index])
                end
            end
        end
        return array
end
