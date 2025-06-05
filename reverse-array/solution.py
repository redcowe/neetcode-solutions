def main(arr: list) -> list:
    new_list = [] * len(arr)
    
    while arr:
        new_list.append(arr[-1])
        arr.pop()
    
    return new_list

print(main([1, 2, 3]))
