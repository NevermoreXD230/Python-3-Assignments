from a04 import openLocks
from a04 import mostTouchableLocker




def test_openLocks_1():
    assert openLocks(10, 10) == 3

def test_openLocks_2():
    assert openLocks(100, 100) == 10

def test_openLocks_3():
    assert openLocks(100, 72) == 34

def test_openLocks_4():
    assert openLocks(70, 100) == 8

def test_openLocks_5():
    assert openLocks(10000, 1000) == 5228

def test_openLocks_6():
    assert openLocks(0, 0) == 0

def test_openLocks_7():
    assert openLocks(0, 3) == 0


def test_openLocks_8():
    assert openLocks(1, 0) == 0


def test_mostTouchableLocker_1():
    assert mostTouchableLocker(10, 10) == 10

def test_mostTouchableLocker_2():
    assert mostTouchableLocker(20, 10) == 20

def test_mostTouchableLocker_3():
    assert mostTouchableLocker(72, 100) == 72

def test_mostTouchableLocker_4():
    assert mostTouchableLocker(100, 70) == 60

def test_mostTouchableLocker_5():
    assert mostTouchableLocker(100, 100) == 96

# if __name__ == "__main__":
#     test_mostTouchableLocker_1()
#     test_mostTouchableLocker_2()
#     test_mostTouchableLocker_3()
#     test_mostTouchableLocker_4()
#     test_mostTouchableLocker_5()

#     test_openLocks_1()
#     test_openLocks_2()
#     test_openLocks_3()
#     test_openLocks_4()
#     test_openLocks_5()
#     test_openLocks_6()
#     test_openLocks_7()
#     test_openLocks_8()
