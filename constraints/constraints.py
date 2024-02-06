def relevant_rows_sum(
    columns: tuple[str, ...],
    table: list[tuple[int, ...]],
    queries: list[tuple[str, str, int]]
) -> int:
    relevant_rows_sum = 0

    for row in table:
        for constr_column, constr_condition, constr_value in queries:
            constr_column_index = columns.index(constr_column)
            value = row[constr_column_index]

            conidition = value > constr_value if constr_condition == ">" else value < constr_value

            if not conidition:
                break
        else:
            relevant_rows_sum += sum(row)
            
    return relevant_rows_sum
