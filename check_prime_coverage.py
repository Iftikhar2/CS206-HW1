# Import the Pytest coverage plugin:
import coverage

# Start code coverage before importing other modules:
cov = coverage.Coverage()
cov.start()

# Main code to be covered----------:

import sys
sys.path.append(sys.path[0] + "/..")

from tests.check_prime import checkPrime

num_entered = int(input("Enter a number : "))
result = checkPrime(num_entered)
print(result)

cov.stop()
cov.save()
cov.html_report(directory='coverage_reports')
