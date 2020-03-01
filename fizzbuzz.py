def fizzbuzz_convert(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    return number


assert fizzbuzz_convert(3) == 'Fizz'
assert fizzbuzz_convert(5) == 'Buzz'
