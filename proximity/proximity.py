def lists_proximity(first_list: list[int], second_list: list[int]):
    min_array_length = min(len(first_list), len(second_list))

    proximity = 0
    
    for i in range(min_array_length):
        if first_list[i] != second_list[i]:
            break

        proximity += 1
    
    return proximity


def two_dim_array_proximity(two_dim_array: list[list[int]]) -> int:
    two_dim_array_len = len(two_dim_array)

    total_proximity = 0

    for i in range(two_dim_array_len):
        for j in range(i + 1, two_dim_array_len):
            total_proximity += lists_proximity(two_dim_array[i], two_dim_array[j])

    return total_proximity
