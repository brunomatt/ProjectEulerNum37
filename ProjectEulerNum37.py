# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage:
# 3797, 797, 97, and 7.
# Similarly we can work from right to left:
# 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
import time # this program takes about 20 seconds to run on my Lenovo Thinkpad
start = time.time()

answer = 0
primes = []
eleven_trunc_primes = []

def sieve_eratosthenes(n):
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return primes

sieve_eratosthenes(1000000)

def deconstruct(num): #turns number into a list of its digits
    digits = [int(k) for k in str(num)]
    return digits

def convert(list): #turns digit list into a number
    num = sum(digit * pow(10,i) for i, digit in enumerate(list[::-1]))
    return (num)

def check_trunc_prime(num):
    truth_test = []
    possible_primes = []
    digits = deconstruct(num)
    for m in range(1,len(str(num))):
        digits.remove(digits[0])
        possible_primes.append(convert(digits))
    digits = deconstruct(num)
    for m in range(1,len(str(num))):
        digits.pop()
        possible_primes.append(convert(digits))
    for j in possible_primes:
        if j in primes:
            truth_test.append(True)
        else:
            truth_test.append(False)
            break
    if all(truth_test):
        return True
    else:
        return False

for num in primes: # cuts run-time in half by eliminating primes with even digits, excluding 2
    even_check = any(char in deconstruct(num) for char in [0,4,6,8])
    if even_check is True:
        primes.remove(num)

for i in primes:
    if check_trunc_prime(i) is True and i > 7:
        eleven_trunc_primes.append(i)
        if len(eleven_trunc_primes) == 11:
            break

answer = sum(i for i in eleven_trunc_primes)

print(answer)

stop = time.time()
print("Time: ", stop - start)