#UnboundLocalError: cannot access local variable 'num' where it is not associated with a value
num = 10

def test_func():
    print("The number is:", num)
    num = 20

test_func()
