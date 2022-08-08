"""
Finding the average of the sum of prime numbers between 1 to a given number(10000)
Philip OlaBisi Ganiyu
10956021
"""
def aveg_ofPrimes():
    sum = 0
    j = 0
    for num in range(1, 10000):
            i = 1
            for i in range(2, num):
                if num % i == 0:
                    i = num
                    break
            if i is not num:
                sum += num
                j += 1 
    float 
    aveg = sum/j  
    print(aveg)
aveg_ofPrimes()