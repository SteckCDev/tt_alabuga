def relevant_rows_sum(
    columns: tuple[str, ...],
    table: list[tuple[int, ...]],
    constraints: list[tuple[str, str, int]]
) -> int:
    relevant_rows_sum = 0

    for row in table:
        for constr_column, constr_condition, constr_value in constraints:
            constr_column_index = columns.index(constr_column)
            value = row[constr_column_index]

            conidition = value > constr_value if constr_condition == ">" else value < constr_value

            if not conidition:
                break
        else:
            relevant_rows_sum += sum(row)
            
    return relevant_rows_sum


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
