numbers = {
        "0" : 0,
        "1" : 1,
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9
    }
def multiply(num1: str, num2: str) -> str:
    int_num1_arr = []
    int_num2_arr = []
    for digit in num1:
        int_num1_arr.append(numbers.get(digit))

    for digit in num2:
        int_num2_arr.append(numbers.get(digit))

    return str(convertToInt(int_num1_arr) * convertToInt(int_num2_arr))

def convertToInt(num: list):
    num.reverse()

    number = 0

    for i in range(0, len(num) , 1):
        number += 10**i * num[i]
    return number
    #get the length of the array, this is how many digits (places) are in the integer
    #for example, if the length of the array is 2, we know the digit is 9 < d < 99
    # if the length is 3, it has to be 99 < d < 999
    # 1, 10, 100, 1000

print(multiply("123", "456"))