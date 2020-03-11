import pytest

def yes_no(arr):
    if(len(arr) <= 2): return arr
    evenIndex = [x for x in arr if (arr.index(x)%2 == 0)]
    oddIndex = [x for x in arr if (arr.index(x)%2 != 0)]
    return evenIndex+yes_no(oddIndex)

def test_single_element_array():
    assert(yes_no(['this', 'code', 'is', 'right', 'the']) == [ 'this', 'is', 'the', 'right', 'code' ])

def test_two_element_array():
    assert(yes_no([1,2]) == [1,2])

def test_three_element_array():
    assert(yes_no([1,2,3]) == [1,3,2])

def test_four_element_array():
    assert(yes_no([1,2,3,4]) == [1,3,2,4])

def test_five_element_array():
    assert(yes_no([1,2,3,4,5]) == [1,3,5,2,4])

def test_six_element_array():
    assert(yes_no([1,2,3,4,5,6]) == [1,3,5,2,6,4])

def test_seven_element_array():
    assert(yes_no([1,2,3,4,5,6,7]) == [1,3,5,7,2,6,4])

def test_eight_element_array():
    assert(yes_no([1,2,3,4,5,6,7,8]) == [1,3,5,7,2,6,4,8])

def test_nine_element_array():
    assert(yes_no([1,2,3,4,5,6,7,8,9]) == [1,3,5,7,9,2,6,4,8])

def test_ten_element_array():
    assert(yes_no([1,2,3,4,5,6,7,8,9,10]) == [1,3,5,7,9,2,6,10,8,4])

    1,3,5,7,9,2,6,10,4,8
    2,4,6,8,10
    4,8

     