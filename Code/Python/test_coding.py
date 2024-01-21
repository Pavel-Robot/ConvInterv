import maincopylibmain
import pytest

def test_nml_118():
    n, m, l = 1, 2, 1
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1"

def test_nml_1():
    n, m, l = 1, 1, 1
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1"
 
def test_nml_2():
    n, m, l = 1, 1, 2
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,2"

def test_nml_3():
    n, m, l = 1, 1, 3
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,2,3"

def test_nml_4():
    n, m, l = 1, 1, 4
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,2,3,4"

def test_nml_4444():
    n, m, l = 2, 1, 3
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,3"

def test_nml_5():
    n, m, l = 2, 1, 4
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,3,2"

def test_nml_6():
    n, m, l = 2, 2, 4
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,3,0"

# не хватает еще одного прогона в цикле, пока не понял почему
def test_nml_7():
    n, m, l = 2, 2, 8
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,3,0,5,2,7,4"

def test_nml_77():
    n, m, l = 2, 2, 10
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,3,0,5,2,7,4,9,6"

def test_nml_777():
    n, m, l = 2, 2, 12
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,3,0,5,2,7,4,9,6,11,8"

def test_nml_8():
    n, m, l = 4, 1, 16
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,0,0,5,2,0,0,9,6,3,0,13,10,7,4"

def test_nml_9():
    n, m, l = 4, 2, 16
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,0,0,5,0,0,0,9,2,0,0,13,6,0,0"

def test_nml_10():
    n, m, l = 4, 3, 16
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,0,0,5,0,0,0,9,0,0,0,13,2,0,0"

def test_nml_11():
    n, m, l = 4, 4, 16
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,0,0,5,0,0,0,9,0,0,0,13,0,0,0"


def test_nml_12():
    n, m, l = 4, 5, 16
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,0,0,5,0,0,0,9,0,0,0,13,0,0,0"

def test_nml_121():
    n, m, l = 4, 5, 17
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,0,0,5,0,0,0,9,0,0,0,13,0,0,0,17"


def test_nml_1211():
    n, m, l = 3, 2, 11
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,0,4,0,0,7,2,0,10,5"


def test_nml_555():
    n, m, l = 2, 5, 27
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,3,0,5,0,7,0,9,0,11,2,13,4,15,6,17,8,19,10,21,12,23,14,25,16,27"

def test_nml_5555():
    n, m, l = 4, 5, 50
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,0,0,5,0,0,0,9,0,0,0,13,0,0,0,17,0,0,0,21,2,0,0,25,6,0,0,29,10,0,0,33,14,0,0,37,18,0,0,41,22,3,0,45,26,7,0,49,30"

def test_nml_9999():
    n, m, l = 7, 5, 43
    output = maincopylibmain.ConvolutionalInterleaver(n, m, l)
    assert output == "1,0,0,0,0,0,0,8,0,0,0,0,0,0,15,0,0,0,0,0,0,22,0,0,0,0,0,0,29,0,0,0,0,0,0,36,2,0,0,0,0,0,43"
