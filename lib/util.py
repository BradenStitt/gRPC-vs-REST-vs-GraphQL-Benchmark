def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(n: int) -> int:
    """Count the number of prime numbers up to n."""
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count
