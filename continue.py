def find_primes(n):
    primes = []
    for num in range(2, n+1):
        for i in range(2, num):
            if num % i == 0:
                continue
        primes.append(num)
    return primes


# get user input for the range
n = int(input("Enter the range: "))

primes = find_primes(n)

# sum the prime numbers
sum = 0
for num in primes:
    sum += num

average = sum / n

print(f"\nPrime numbers:{find_primes(n)}")
print("Sum of all prime numbers:", sum)
print("Average of all prime numbers:", average)
