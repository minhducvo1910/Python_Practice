'''UNIT TEST: test for individual unit of the program'''

def main():
    num = int(input("What is x square?"))
    print("x square is", square(num))

def square(x):
    return x+x
if __name__ == "__main__":
    main()

''' "assert" keyword: find AssertionError'''
'''Using pytest module: py -m pytest file_name'''
'''from UnitTest import square
import pytest

def test_square():
    assert square(2) == 4
    assert square(3) == 9  #Find assertion error

def test_str():
    with pytest.raises(TypeError):  ()
        square("cat")
def test_float_conversion:
    assert convert(0.001) == pytest.approx(14903985.049, abs=0.1)'''