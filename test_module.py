import pytest
import budget


@pytest.fixture()
def input_value():
    value = ["amount_example", "description_example"]
    return value


# @pytest.mark.skip
def test_deposit(input_value):
    assert budget.Category.deposit(input_value[0], input_value[1]) == {"amount": "amount_exampl", "description": "description_example"}

