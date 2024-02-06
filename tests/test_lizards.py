import pytest

from tasks.lizards import lizard_existence_days, lizard_existence_days_no_datetime


@pytest.mark.parametrize(
    "start_exact, end_exact, result_days, result_seconds_left",
    [
        (
            (980, 2, 12, 10, 30, 1),
            (980, 3, 1, 10, 31, 37),
            17,
            96
        ),
        (
            (1001, 5, 20, 14, 15, 16),
            (9009, 9, 11, 12, 21, 11),
            2923033,
            79555
        ),
    ]
)
def test_lizard_existence_time(
        start_exact: tuple[int, int, int, int, int, int],
        end_exact: tuple[int, int, int, int, int, int],
        result_days: int,
        result_seconds_left: int
) -> None:
    assert (result_days, result_seconds_left) == lizard_existence_days(
        start_exact=start_exact,
        end_exact=end_exact
    )

    # must have the same behaviour
    assert (result_days, result_seconds_left) == lizard_existence_days_no_datetime(
        start_exact=start_exact,
        end_exact=end_exact
    )
