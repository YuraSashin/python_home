
from seminar6.portfolio import calculate_portfolio_return, calculate_portfolio_value, get_most_profitable_stock


my_dick1 = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
my_dick2 = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
a = 10000
b = 15000

summa = calculate_portfolio_value(my_dick1, my_dick2)
print(summa)

progress_ = calculate_portfolio_return(a,b)
print(progress_)

max_ = get_most_profitable_stock(my_dick1,my_dick2)
print(max_)