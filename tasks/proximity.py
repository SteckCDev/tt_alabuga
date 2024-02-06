def lists_proximity(first_list: tuple[int, ...], second_list: tuple[int, ...]):
    proximity = 0

    for f, s in zip(first_list, second_list):
        if f != s:
            return proximity

        proximity += 1

    return proximity


def two_dim_array_proximity(two_dim_array: list[tuple[int, ...]]) -> int:
    """
    Оптимизированный вариант, первое решение доступно в истории коммитов
    """
    total_proximity = 0

    for i, first_list in enumerate(two_dim_array):
        for second_list in two_dim_array[i + 1:]:
            total_proximity += lists_proximity(first_list, second_list)

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
