from main import is_even, is_odd, is_prime

def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-4) is True

def test_is_odd():
    assert is_odd(2) is False
    assert is_odd(3) is True
    assert is_odd(0) is False
    assert is_odd(-5) is True

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(13) is True
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-7) is False
