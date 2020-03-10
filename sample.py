def FizzBuzz(n):
    ret_str = ""
    if n % 3 == 0:
        ret_str += "Fizz"
    if n % 5 == 0:
        ret_str += "Buzz"
    if ret_str == "":
        return n
    return ret_str