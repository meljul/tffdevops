from calculatrice import addition

Task = addition(2,2)

def test_addition():
    t1 = Task
    t2 = 2 + 2
    assert t1 == t2