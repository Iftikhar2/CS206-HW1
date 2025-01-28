def checkPrime(num: int):
  # Prime numbers are greater than 1
    if num > 1:
      
        # check whether the entered number is divisible
        # by any number between 2(inclusive) and n/2.
        for i in range(2, (num//2)+1):
          
            # If divsible, then the entered number is not prime.
            if (num % i) == 0:
                return(str(num) + " is not a prime number")
        else:
            return(str(num) + " is a prime number")
    # Numbers less than 2 are not primes
    else:
        return(str(num) + " is not a prime number")

