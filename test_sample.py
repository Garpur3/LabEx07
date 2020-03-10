from sample import FizzBuzz

numbers = [23, 20, 21, -21, 10, 15, 45, -45, -20, 2, 100]

values = [23, "Buzz", "Fizz", -21, "Buzz", "FizzBuzz", "FizzBuzz", -45, -20, 2, "Buzz"]

for number, value in zip(numbers, values):
    foo_val = FizzBuzz(number)
    if foo_val == value:
        print(f"Function works for {number} and returns {foo_val}")
    else:
        print(f"Unexpected return value for {number}: {foo_val}")