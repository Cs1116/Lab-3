import employee_info

def test_get_employees_by_age_range():
    age_lower_limit = 30
    age_upper_limit = 40
    result = employee_info.get_employees_by_age_range(age_lower_limit,age_upper_limit)
    test = [
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
]
    assert (result == test)

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    test = 60167
    assert (result == test)

def test_get_employees_by_dept():
    department = "Engineering"
    result = employee_info.get_employees_by_dept(department)
    test = [
        {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]
    assert (result == test)