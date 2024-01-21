include("code.jl") # сверточное перемежение - кодировка
include("decode.jl") # сверточное перемежение - декодировка

using Plots

# Функция для замера времени и памяти
# (без множественного эксперимента - по 1 измерению на 1 точку)
# для повторений btime..
function timeof(counter::Int64)
    masTime = Float64[] # Для замера времени в сек
    masBytes = Int64[] # Для замера памяти в байтах
    for size=1:4:counter
        #r = rand(Int8, size)
        x = collect(1:size)
        x = ConvolutionalInterleaver(x, 2, 2)
        time_bytes = @timed decode(x, 2, 2)
        push!(masTime, time_bytes.time)
        push!(masBytes, floor(Int64, time_bytes.bytes/1024))
    end
    
    return masTime, masBytes
end

Num = 1024
t_b = timeof(Num)
pp1 = scatter(t_b[1], title="Оценка временной сложности", xlabel="sizeInVector", ylabel="sec")
#pp2 = scatter(t_b[2], title="Оценка пространственной сложности", xlabel="sizeInVector", ylabel="Mb")

Plots.gui(plot(pp1, legend=false))
println("!!!Нажмите клавишу чтобы завершить ввод!!!")
readline()