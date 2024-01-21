using Test

include("code.jl") # Функция кодировки

# хотя бы показывает строку теста, где не прошёл
# В Linux удобно оказалось:
# julia test_code.jl | grep "Expression: ConvolutionalInterleaver("
@testset "ConvInterlv" begin
    @test ConvolutionalInterleaver(2, 1, 8) == "1,0,3,2,5,4,7,6"
    @test ConvolutionalInterleaver(1, 2, 1) == "1"
    @test ConvolutionalInterleaver(1, 1, 1) == "1"
    @test ConvolutionalInterleaver(1, 1, 2) == "1,2"
    @test ConvolutionalInterleaver(1, 1, 3) == "1,2,3"
    @test ConvolutionalInterleaver(1, 1, 4) == "1,2,3,4"
    @test ConvolutionalInterleaver(2, 1, 3) == "1,0,3"
    @test ConvolutionalInterleaver(2, 1, 4) == "1,0,3,2"
    @test ConvolutionalInterleaver(2, 2, 4) == "1,0,3,0"
    @test ConvolutionalInterleaver(2, 2, 8) == "1,0,3,0,5,2,7,4"
    @test ConvolutionalInterleaver(2, 2, 10) == "1,0,3,0,5,2,7,4,9,6"
    @test ConvolutionalInterleaver(2, 2, 12) == "1,0,3,0,5,2,7,4,9,6,11,8"
    @test ConvolutionalInterleaver(4, 1, 16) == "1,0,0,0,5,2,0,0,9,6,3,0,13,10,7,4"
    @test ConvolutionalInterleaver(4, 2, 16) == "1,0,0,0,5,0,0,0,9,2,0,0,13,6,0,0"
    @test ConvolutionalInterleaver(4, 3, 16) == "1,0,0,0,5,0,0,0,9,0,0,0,13,2,0,0"
    @test ConvolutionalInterleaver(4, 4, 16) == "1,0,0,0,5,0,0,0,9,0,0,0,13,0,0,0"
    @test ConvolutionalInterleaver(4, 5, 16) == "1,0,0,0,5,0,0,0,9,0,0,0,13,0,0,0"
    @test ConvolutionalInterleaver(4, 5, 17) == "1,0,0,0,5,0,0,0,9,0,0,0,13,0,0,0,17"
    @test ConvolutionalInterleaver(3, 2, 11) == "1,0,0,4,0,0,7,2,0,10,5"
    @test ConvolutionalInterleaver(2, 5, 27) == "1,0,3,0,5,0,7,0,9,0,11,2,13,4,15,6,17,8,19,10,21,12,23,14,25,16,27"
    @test ConvolutionalInterleaver(4, 5, 50) == "1,0,0,0,5,0,0,0,9,0,0,0,13,0,0,0,17,0,0,0,21,2,0,0,25,6,0,0,29,10,0,0,33,14,0,0,37,18,0,0,41,22,3,0,45,26,7,0,49,30"
    @test ConvolutionalInterleaver(7, 5, 43) == "1,0,0,0,0,0,0,8,0,0,0,0,0,0,15,0,0,0,0,0,0,22,0,0,0,0,0,0,29,0,0,0,0,0,0,36,2,0,0,0,0,0,43"
end
