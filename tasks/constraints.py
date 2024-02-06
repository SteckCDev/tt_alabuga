def relevant_rows_sum(
    columns: tuple[str, ...],
    table: list[tuple[int, ...]],
    constraints: list[tuple[str, str, int]]
) -> int:
    """
    Оптимизированный вариант, первое решение доступно в истории коммитов
    """
    columns_indices = {column_value: column_id for column_id, column_value in enumerate(columns)}
    rows_passed_condition_indicies: list[int] = [i for i, _ in enumerate(table)]

    for c_column, c_condition, c_value in constraints:
        c_column_index = columns_indices[c_column]

        for row_id in rows_passed_condition_indicies:
            row_value = table[row_id][c_column_index]

            if row_value <= c_value if c_condition == ">" else row_value >= c_value:
                rows_passed_condition_indicies.remove(row_id)

    return sum(sum(table[row_id]) for row_id in rows_passed_condition_indicies)


def main() -> None:
    columns: list[str] = []
    table: list[tuple[int, ...]] = []
    constraints: list[tuple[str, str, int]] = []

    quantities_caption = "Укажите: количество строк, стобцов и ограничений " \
                         "(разделяйте значения пробелами: 'строки столбцы ограничения'): "
    column_name_caption = "Задайте имя столбцу {i}: "
    row_value_caption = "Укажите значение для столбца {j} в строке {i}: "
    constr_caption = "Задайте {i} ограничение ('имя_столбца [< | >] число'): "

    rows_quantity, columns_quantity, constr_quantity = map(int, input(quantities_caption).split())

    for i in range(1, columns_quantity + 1):
        columns.append(input(column_name_caption.format(i=i)))

    for i in range(rows_quantity):
        row: list[int] = []

        for j in range(columns_quantity):
            row.append(int(input(row_value_caption.format(i=i, j=j))))
        
        table.append(tuple(row))
    
    for i in range(constr_quantity):
        constr_column, constr_condition, constr_value = input(constr_caption.format(i=i)).split()

        constraints.append(
            (constr_column, constr_condition, int(constr_value))
        )
        
    result = relevant_rows_sum(
        columns=tuple(columns),
        table=table,
        constraints=constraints
    )

    print(f"Сумма всех удовлетворяющих запросу строк: {result}")


if __name__ == "__main__":
    main()
