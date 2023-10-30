import Lab2.bmi

def test_bmi_normal_weight():
    test=0
    w=Lab2.bmi.calculate_bmi(height=1.71,weight=55)
    assert(test==w)

def test_bmi_under_weight():
    test = -1
    w=Lab2.bmi.calculate_bmi(height=1.71,weight=50)
    assert(test==w)

def test_bmi_over_weight():
    test = 1
    w=Lab2.bmi.calculate_bmi(height=1.71,weight=100)
    assert(test==w)