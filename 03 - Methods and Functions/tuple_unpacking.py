stock_prices = [("APPL", 200), ("GOOG", 400), ("GOOG", 100)]

for ticker, price in stock_prices:
    print(ticker)
    print(price)


work_hour = [("Abby", 100), ("Billy", 4000), ("Cassie", 800)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ""

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee

    return (employee_of_month, current_max)


name, hours = employee_check(work_hour)
print(name)
print(hours)
