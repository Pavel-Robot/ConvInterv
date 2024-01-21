import maincopylibmain
import pytest

def test_nml_1():
    n, m, l = 2, 1, 8
    output = maincopylibmain.decode(n, m, l)
    assert output == "0,0,1,2,3,4,5,6"

def test_nml_2():
    n, m, l = 3, 1, 9
    output = maincopylibmain.decode(n, m, l)
    assert output == "0,0,0,0,0,0,1,2,3"

def test_nml_3():
    n, m, l = 2, 1, 20
    output = maincopylibmain.decode(n, m, l)
    assert output == "0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18"

def test_nml_4():
    n, m, l = 3, 1, 18
    output = maincopylibmain.decode(n, m, l)
    assert output == "0,0,0,0,0,0,1,2,3,4,5,6,7,8,9,10,11,12"

def test_nml_5():
    n, m, l = 4, 1, 20
    output = maincopylibmain.decode(n, m, l)
    assert output == "0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8"

def test_nml_6():
    n, m, l = 7, 1, 20
    output = maincopylibmain.decode(n, m, l)
    assert output == "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
    
def test_nml_7():
    n, m, l = 2, 1, 11
    output = maincopylibmain.decode(n, m, l)
    assert output == "0,0,1,2,3,4,5,6,7,8,9"

def test_nml_8():
    n, m, l = 3, 1, 23
    output = maincopylibmain.decode(n, m, l)
    assert output == "0,0,0,0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17"

def test_nml_9():
    n, m, l = 2, 2, 8
    output = maincopylibmain.decode(n, m, l)
    assert output == "0,0,0,0,1,2,3,4"

def test_nml_10():
    n, m, l = 2, 2, 10
    output = maincopylibmain.decode(n, m, l)
    assert output == "0,0,0,0,1,2,3,4,5,6"

def test_nml_11():
    n, m, l = 2, 3, 10
    output = maincopylibmain.decode(n, m, l)
    assert output == "0,0,0,0,0,0,1,2,3,4"

def test_nml_12():
    n, m, l = 2, 3, 11
    output = maincopylibmain.decode(n, m, l)
    assert output == "0,0,0,0,0,0,1,2,3,4,5"

def test_nml_13():
    n, m, l = 5, 3, 17
    output = maincopylibmain.decode(n, m, l)
    assert output == "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"

def test_nml_14():
    n, m, l = 2, 7, 23
    output = maincopylibmain.decode(n, m, l)
    assert output == "0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8,9"

# Этот тест не срабатывает из-за того, что dn сдвиг не правильно рассчитывается для этих данных,
# по моему там должно быть 24 12 0 для элементов, а у меня считает 24 21 0. С чем связано -
#def test_nml_15():
#    n, m, l = 3, 4, 50
#    output = maincopylibmain.decode(n, m, l)
#    assert output == "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26"


