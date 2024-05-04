import employee_info as employ

def test_get_employees_by_age_range():
    expected_result=[{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    test_result=employ.get_employees_by_age_range(20,31)
    assert(test_result==expected_result)

def test_calculate_average_salary():
    expected_result=str(60166.67)
    assert(employ.calculate_average_salary()==expected_result)

def test_get_employees_by_dept():
    expected_result=[{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    test_result=employ.get_employees_by_dept("Engineering")
    assert(expected_result==test_result)

    