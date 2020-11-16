from a03 import calculateProfit
from a03 import chocolatePrice



def test_calculateProfit_zero_check_1():
    assert calculateProfit(2, 0) == "Not Possible"

def test_calculateProfit_zero_check_2():
    assert calculateProfit(0, 4) == "Not Possible"


def test_calculateProfit_zero_check_all():
    assert calculateProfit(0, 0) == "Not Possible"


def test_calculateProfit_str_check_1():
    assert calculateProfit("4", 1) == "Not Possible"

def test_calculateProfit_str_check_2():
    assert calculateProfit(1, "2") == "Not Possible"

def test_calculateProfit_str_check_all():
    assert calculateProfit("2", "3") == "Not Possible"

 



def test_chocolatePrice_1():
    assert chocolatePrice(55, 15) == 5

def test_chocolatePrice_2():
    assert chocolatePrice(99, 18) == 9


def test_chocolatePrice_3():
    assert chocolatePrice(30, 12) == 6

def test_chocolatePrice_4():
    assert chocolatePrice(50, 10) == 10


# if __name__ == "__main__":
#     test_calculateProfit_str_check_1()
#     test_calculateProfit_str_check_2()
#     test_calculateProfit_str_check_all()
#     test_calculateProfit_zero_check_1()
#     test_calculateProfit_zero_check_2()
#     test_calculateProfit_zero_check_all()

#     test_chocolatePrice_1()
#     test_chocolatePrice_2()
#     test_chocolatePrice_3()
#     test_chocolatePrice_4()
