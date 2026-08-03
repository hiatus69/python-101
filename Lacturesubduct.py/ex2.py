def generate_primes(num):
    primes = []
    for n in range(2, num + 1):
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes

print(generate_primes(10))
print(generate_primes(20))
print(generate_primes(1))
print(generate_primes(2))

# def generate_prime_numbers(n):
#     primes = []
#     for num in range(2, n + 1):
#         is_prime = True
#         for prime in primes:
#             if prime * prime > num:
#                 break
#             if num % prime == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num) #append() คือการเพิ่มค่าตัวเลขเข้าไปในลิสต์ primes
#     return primes