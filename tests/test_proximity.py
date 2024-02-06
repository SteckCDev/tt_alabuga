import pytest

from proximity import two_dim_array_proximity


@pytest.mark.parametrize(
    "two_dim_array, result",
    [
        (
            [
                [1, 2],
                [1, 3],
                [1, 2, 3]
            ],
            4
        ),
        (
            [
                [5],
                [1, 2],
                [5, 1, 2]
            ],
            1
        ),
    ]
)
def test_relevant_rows_sum(two_dim_array: list[list[int]], result: int) -> None:
    assert result == two_dim_array_proximity(two_dim_array=two_dim_array)
