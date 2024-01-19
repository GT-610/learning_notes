from employee import Employee
import pytest

@pytest.fixture
def emp0():
    emp0=Employee("Ming","Wang",1145)
    return emp0

def test_give_default_raise(emp0):
    emp0.give_raise()
    assert emp0.salary==6145

def test_give_custom_raise(emp0):
    emp0.give_raise(2000)
    assert emp0.salary==3145