include("code_func.jl") # Функции для этого блока


# Реализация блока сверточного перемежения (основная функция)
# x - входной вектор (состоит из целых чисел)
# n - количество регистров, m - шаг 
# регистров(на каком x[i] будет использоваться регистр)
#function ConvolutionalInterleaver(x::Vector, n::Int64, m::Int64, l::Int64) # для тестирования
function ConvolutionalInterleaver(x::Vector, n::Int64, m::Int64)

    l = length(x)
    chunk_count = myround(length(x)/n)
    x = division_x(x, chunk_count, n) # Разделяем поток битов на блоки количества chunk_count
    

    all_y = []
    all_r = []
    N = myround(l/n); if N < 1 N = 1 end
    
    for j=2:N+1
        x_out_first, reg_first = registry_one(x[j-1])

        y = [x_out_first]
        r = [deepcopy(reg_first)]

        index = 1
        for i=j:length(x)
            x_out, reg, index = registry_two(x[i], last(r), index, m)
            push!(y, x_out)
            push!(r, deepcopy(reg))
        end

        push!(all_y, y)
        push!(all_r, r)
    end

    text = ""
    if length(all_y) != 1
        ans = shift(all_y, n, m, l)
        #text = join(vcat(ans...), ",")
    else
        ans = all_y
        #text = string(ans[1][1][1])
    end

    #return text # для тестирования
    return vcat(ans...) # Как в Matlab
end

#size = 8192
#x = collect(1:size)
#ans = @timed ConvolutionalInterleaver(x, 2, 2)
#println(ans.time)
# lenx = 2; n=2; m=2; time=0.25s
# lenx = 1024; n=2; m=2; time=0.5s
# lenx = 2048; n=2; m=2; time=1.14s
# lenx = 4096; n=2; m=2; time=3.7s
# lenx = 65536; n=2; m=2; time=23.16s
# many memory use ;( При больших n ситуация улучшается.