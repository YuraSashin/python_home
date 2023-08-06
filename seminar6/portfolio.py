# Расчет общей стоимости портфеля акций: Функция calculate_portfolio_value(stocks: dict, prices: dict) -> float 
# принимает два аргумента: stocks - словарь, где ключами являются символы акций (например, "AAPL" для Apple Inc.), 
# и значениями - количество акций каждого символа. prices - словарь, где ключами являются символы акций,
# а значениями - текущая цена каждой акции. Функция должна вернуть общую стоимость портфеля акций на основе количества акций и их текущих цен

def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    sum = 0
    for key in stocks:
        sum += stocks[key]

    for key2 in prices:
        sum += prices[key2]
    
    return sum

# Расчет доходности портфеля: Функция calculate_portfolio_return(initial_value: float, current_value: float) -> float
# принимает два аргумента: initial_value - начальная стоимость портфеля акций. current_value - текущая стоимость портфеля акций.
# Функция должна вернуть процентную доходность портфеля. 

def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    progress = initial_value / current_value * 100
    return progress

# Определение наиболее прибыльной акции: Функция get_most_profitable_stock(stocks: dict, prices: dict) -> str
# принимает два аргумента: stocks - словарь с акциями и их количеством. prices - словарь с акциями и их текущими ценами.
# Функция должна вернуть символ акции (ключ), которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью.
# Начальная стоимость - первый вызов calculate_portfolio_value, данные из этого вызова следует сохранить в защищенную переменную на уровне модуля.

def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    max = 0
    new_dict = stocks | prices

    for key in new_dict:
        if(max < new_dict[key]):
            max = new_dict[key]  

    max_str = str(list(new_dict.keys())[list(new_dict.values()).index(max)])
    
    return max_str                                                     