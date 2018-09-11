"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months_paid = int(input("How many months? "))

    for month in range(1, months_paid + 1):
        income = float(input("Enter income for month {}:" .format(month)))
        incomes.append(income)

    Income_Report(incomes)

def Income_Report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month + 1, income, total))

    return incomes

main()