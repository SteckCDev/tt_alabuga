def lists_proximity(first_list: tuple[int, ...], second_list: tuple[int, ...]):
    min_array_length = min(len(first_list), len(second_list))

    proximity = 0
    
    for i in range(min_array_length):
        if first_list[i] != second_list[i]:
            break

        proximity += 1
    
    return proximity


def two_dim_array_proximity(two_dim_array: list[tuple[int, ...]]) -> int:
    two_dim_array_len = len(two_dim_array)

    total_proximity = 0

    for i in range(two_dim_array_len):
        for j in range(i + 1, two_dim_array_len):
            total_proximity += lists_proximity(two_dim_array[i], two_dim_array[j])

    return total_proximity


def main() -> None:
    two_dim_array: list[tuple[int, ...]] = []

    lists_qunatity_caption = "Пожалуйста, обозначьте ожидаемое количество массивов: "
    list_length_caption = "Задайте размер текущего массива: "
    list_value_caption = "Введите элемент текущего массива: "

    lists_quantity = int(input(lists_qunatity_caption))

    for _ in range(lists_quantity):
        list_length = int(input(list_length_caption))
        actual_list: list[int] = []

        for _ in range(list_length):
            actual_list.append(
                int(input(list_value_caption))
            )
        
        two_dim_array.append(
            tuple(actual_list)
        )

    result = two_dim_array_proximity(two_dim_array=two_dim_array)

    print(f"Суммарная близость переданных массивов равна {result}")


if __name__ == "__main__":
    main()
