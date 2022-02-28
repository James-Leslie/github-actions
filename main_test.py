from main import add_two, multiply_two


def test_add():
    assert add_two(3, 4) == 7


def test_multiply():
    assert multiply_two(2, 2) == 4
    assert multiply_two(2, 3) == 6
