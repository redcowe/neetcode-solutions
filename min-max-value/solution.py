import math
def main(arr: list) -> list:
    min_value, max_value = math.inf, - math.inf
    for value in arr:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
        continue
    return [min_value, max_value]

print(main([2, 1, 6, 89, 1]))

def test(arr: list) -> list:
    arr.sort()
    return [arr[0], arr[-1]]

print(test([2, 1, 6, 89, 1]))