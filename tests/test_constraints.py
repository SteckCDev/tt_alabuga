import pytest

from tasks.constraints import relevant_rows_sum


@pytest.mark.parametrize(
    "columns, table, constraints, result",
    [
        (
            ("a", "b"),
            [
                (1, 1),
                (2, 2)
            ],
            [
                ("a", "<", 3),
                ("b", ">", 1),
                ("b", "<", 3)
            ],
            4
        ),
        (
            ("a", "b", "c"),
            [
                (50, 150, 40),
                (70, 20, 0),
                (70, 60, 90),
                (80, 60, 100),
            ],
            [
                ("a", "<", 80),
                ("b", ">", 20)
            ],
            460
        ),
    ]
)
def test_relevant_rows_sum(
        columns: tuple[str, ...],
        table: list[tuple[int, ...]],
        constraints: list[tuple[str, str, int]],
        result: int
) -> None:
    assert result == relevant_rows_sum(
        columns=columns,
        table=table,
        constraints=constraints
    )
