from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(6, 2)) == 6
    ), "sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(6, 2) == [3, 3]
    ), "should be split into equal parts when value divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(5, 1) == [5]
    ), "should be equal to value when split 1."


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(5, 4) == [1, 1, 1, 2]
    ), "parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(1, 5) == [0, 0, 0, 0, 1]
    ), "should add zeros when value is less than number of part"
