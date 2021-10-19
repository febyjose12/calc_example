""" content of calculator.py#"""


def inc(x_value):
    """ Increment F unction adds on e to the x_value"""
    return x_value + 1


def test_answer():
    """This Tests the function"""
    assert inc(4) == 5
