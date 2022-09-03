ledger = []


class Category:

    def deposit(self, amount, description):
        ledger.append({"amount": amount, "description": description})
        return ledger


def create_spend_chart(categories):
    pass


if __name__ == "__main__":
    scc = Category()
    scc.deposit("amount_example", "description_example")
    print(scc.deposit("amount_example", "description_example"))
