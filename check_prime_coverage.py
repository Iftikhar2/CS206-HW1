# Import the Pytest coverage plugin:
import coverage

# Start code coverage before importing other modules:
cov = coverage.Coverage()
cov.start()

# Main code to be covered----------:

import sys
sys.path.append(sys.path[0] + "/..")

from check_prime import checkPrime

while True:
    try:
        num_entered = int(input("Enter an integer greater than 1: "))
        if num_entered < 2:
            raise ValueError("Enter an integer greater than 1:")
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter an integer greater than 1.")
        
result = checkPrime(num_entered)
print(result)

cov.stop()
cov.save()
cov.html_report(directory='coverage_reports')
