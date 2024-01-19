from employee import Employee

def test_give_default_raise():
    emp0=Employee("Ming","Wang",1145)
    emp0.give_raise()
    assert emp0.salary==6145

def test_give_custom_raise():
    emp0=Employee("Ming","Wang",1145)
    emp0.give_raise(2000)
    assert emp0.salary==3145