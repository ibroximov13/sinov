def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(n):
    if n < 0:
        return
    print_primes(n-1)
    if is_prime(n):
        print(n)

# Foydalanish
print_primes(10)
