import Lab2.Lab2


def test_find_mini_maxi():
    x = []
    arr = [1000, 45, 569, 349, 659, 293, 0]
    x = Lab2.Lab2.find_min_max(arr)
    result = [0,1000]
    assert (x == result)

def test_calculate_average():
    arr = [2, 2, 2, 4, 4, 4, 3]
    result = 3
    x = Lab2.Lab2.calc_average(arr)
    assert (x == result)

def test_calculate_median_temperature():
    arr = [2, 45, 7, 20, 5, 28, 31, 50, 32, 32]
    result = 29.5
    x = Lab2.Lab2.calc_median_temperature(Lab2.Lab2.sort_temperature(arr))
    assert (x == result)