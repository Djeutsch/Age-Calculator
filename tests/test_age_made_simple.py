import pytest
from age_made_simple.age_calculator import AgeCalculator


VALID_DATE_OF_BIRTH = "1990-02-05"
INVALID_DATE_OF_BIRTH = "1990-2-57"


@pytest.fixture
def age_calculator():
    return AgeCalculator()

#
def test_valid_calculate_age(age_calculator):
    assert age_calculator.calculate_age(VALID_DATE_OF_BIRTH) == 33
    
def test_invalid_calculate_age(age_calculator):
    with pytest.raises(Exception):
        age_calculator.calculate_age(INVALID_DATE_OF_BIRTH)
#
def test_valid_day_of_week(age_calculator):
    assert age_calculator.day_of_week(VALID_DATE_OF_BIRTH) == "Monday"
    
def test_invalid_day_of_week(age_calculator):
    with pytest.raises(Exception):
        age_calculator.calculate_day_of_weekage(INVALID_DATE_OF_BIRTH)