import pytest

from budget import Category


@pytest.fixture()
def input_value():
    value = ["amount_1", "description_1", "amount_2", "description_2", "amount_3", "description_3"]
    return value


def test_two_deposit(input_value):
    l = [{"amount": input_value[0], "description": input_value[1]},
         {"amount": input_value[2], "description": input_value[3]}]
    sc2 = Category()

    sc2.deposit(input_value[0], input_value[1])

    assert sc2.deposit(input_value[2], input_value[3]) == l


# @pytest.mark.skip
def test_one_deposit(input_value):

    sc = Category()
    l=[{'amount': input_value[0], 'description': input_value[1]}]

    assert sc.deposit(input_value[0], input_value[1]) == l

# if __name__ == "__main__":
#     test__deposit(input_value)
