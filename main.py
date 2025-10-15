def is_even(n):
    """Return True if n is even, False otherwise"""
    return n % 2 == 0

def is_odd(n):
    """Return True if n is odd, False otherwise"""
    return n % 2 != 0

def is_prime(n):
    """Return True if n is a prime number, False otherwise"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    numbers = [2, 3, 4, 5, 10, 13]
    for num in numbers:
        print(f"Number: {num}")
        print(f"  Even? {is_even(num)}")
        print(f"  Odd? {is_odd(num)}")
        print(f"  Prime? {is_prime(num)}\n")
