from datetime import datetime
from typing import Final


year = month = day = hour = miunute = second = int


SECONDS_IN_DAY: Final[int] = 24 * 3600
DAYS_IN_MONTH: Final[tuple[int, ...]] = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def lizard_existence_days(
    start_exact: tuple[year, month, day, hour, miunute, second],
    end_exact: tuple[year, month, day, hour, miunute, second],
) -> tuple[int, int]:
    def days_added_by_leap_years(start_year: int, end_year: int) -> int:
        def is_leap_year(year: int) -> bool:
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        return sum(
            int(is_leap_year(year)) for year in range(start_year, end_year + 1)
        )
    
    start_date, end_date = datetime(*start_exact), datetime(*end_exact)

    total_seconds = (end_date - start_date).total_seconds()

    days_existed = int(total_seconds // (24 * 60 * 60)) - days_added_by_leap_years(start_exact[0], end_exact[0])
    seconds_left = int(total_seconds % (24 * 60 * 60))

    return days_existed, seconds_left


def lizard_existence_days_no_datetime(
    start_exact: tuple[year, month, day, hour, miunute, second],
    end_exact: tuple[year, month, day, hour, miunute, second],
) -> tuple[int, int]:
    def convert_to_seconds(exact: tuple[year, month, day, hour, miunute, second]) -> int:
        """
        Potato code here
        """
        # seconds, minutes, hours
        seconds = exact[5] + exact[4] * 60 + exact[3] * 3600

        # days, months, years
        seconds += exact[2] * SECONDS_IN_DAY
        seconds += sum(
            DAYS_IN_MONTH[i] * SECONDS_IN_DAY for i in range(exact[1] - 1)
        )
        seconds += exact[0] * 365 * SECONDS_IN_DAY

        return seconds
    
    start_seconds, end_seconds = convert_to_seconds(start_exact), convert_to_seconds(end_exact)

    seconds_difference = end_seconds - start_seconds

    days_existed = seconds_difference // (SECONDS_IN_DAY)
    seconds_left = seconds_difference % (SECONDS_IN_DAY)

    return days_existed, seconds_left


def main() -> None:
    caption = "Введите дату (разделяйте числа пробелом - 'год месяц день час минута секунда'): "

    start_exact: tuple[int, int, int, int, int, int] = tuple(map(int, input(caption).split()))
    end_exact: tuple[int, int, int, int, int, int] = tuple(map(int, input(caption).split()))

    days_existed, seconds_left = lizard_existence_days(
        start_exact=start_exact,
        end_exact=end_exact
    )

    print(
        f"Ящеры наслаждались вином сорта Мерло из солнечной долины Чили {days_existed} дней и {seconds_left} секунд"
    )

if __name__ == "__main__":
    main()
