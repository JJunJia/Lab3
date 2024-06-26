import Lab2.bmi as bmi

def test_bmi_over_weight():
    expected_result=1
    test_result = bmi.calculate_bmi (1.7,90) 
    assert (test_result==expected_result) #assert (bmi.calculate_bmi (1.7, 90)==1)

def test_bmi_normal_weight():
    expected_result=0
    test_result = bmi.calculate_bmi (1.7,60)
    assert (test_result==expected_result) #assert (bmi.calculate_bmi (1.7, 60)==0)

def test_bmi_under_weight():
    expected_result=-1
    test_result = bmi.calculate_bmi (1.7,45)
    assert (test_result==expected_result) #assert (bmi.calculate_bmi (1.7, 45)==-1)

