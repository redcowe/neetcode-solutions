def main(arr: list, target: int) -> list:
    #store values in array in arr[i]: i format
    hash_map = dict()
    #iterate over values in arr
    for value in arr:
        t = target - value
        if t in hash_map:
            return [hash_map.get(t), value]
        else:
            hash_map[value] = value
    #check if target - arr[i] is in hash map
    #if in hash map return the value in the hash map return hash_map.get(target - arr[i]) and i

    return []


print(main([1, -1, 5, -5], 0))