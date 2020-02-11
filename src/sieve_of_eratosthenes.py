def sieve_of_erat(n):
    sieve = [{"num": x, "num_type": "prime"} for x in range(0,n + 1)]
    step = 2
    
    sieve[0] = {"num": 0, "num_type": "?"}
    sieve[1] = {"num": 1, "num_type": "?"}

    step = 2 # sieve of erat starts by counting from 2 to n by multiples of 2 and marks them as composite except the first multiple
                  # then, it does the same with 3 and keeps incrementing this number and repeating until the second multiple is larger than n
                  # n being the number we're finding the prime/composite numbers up to and including
    
    while step <= (1/2 * n): # stop at half of n because anything more than 1/2n times 2 will be greater than n
        for mult in range(step + step, n + 1, step): #count in multiples of step, ignoring the first because that would be a multiple of 1, 
                                                                           #e.g. 2 * 1 <- multiple of 2 but only times 1 which doesn't make it composite, 2 * 2 <divisible by 2 (composite), 2 * 3, etc
                                                                           #e.g. 6 * 1 <- divisible by 3 and 2 but marked as composite in former iteration of while loop, 6 * 2 divisible by 6, etc

            sieve[mult]["num_type"] = "composite" # the first element in the array is 0 so i'm not subtracting 1
        step += 1
    
    return sieve

n = int(input("Enter a num: "))
sieve = sieve_of_erat(n)

for ele in sieve:
    print(ele)