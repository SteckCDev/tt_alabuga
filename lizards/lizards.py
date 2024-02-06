from datetime import datetime


year = month = day = hour = miunute = second = int


def days_added_by_leap_years(start_year: int, end_year: int) -> int:
    def is_leap_year(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    return sum(
        int(is_leap_year(year)) for year in range(start_year, end_year + 1)
    )


def lizard_existence_days(
    start_exact: tuple[year, month, day, hour, miunute, second],
    end_exact: tuple[year, month, day, hour, miunute, second],
) -> tuple[int, int]:
    start_date, end_date = datetime(*start_exact), datetime(*end_exact)

    total_seconds = (end_date - start_date).total_seconds()

    days_existed = int(total_seconds // (24 * 60 * 60)) - days_added_by_leap_years(start_exact[0], end_exact[0])
    seconds_left = int(total_seconds % (24 * 60 * 60))

    return days_existed, seconds_left
