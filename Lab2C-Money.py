dollars = 0.0
convert_rate = 0.0
item_cost = 0.0
currency = "EUR"
print('What currency is being converted? (e.g. EUR, GBP, CAD)')
currency = str(input('CURRENCY_TO_CONVERT>'))
print('What is the conversion rate for today\'s currency to US dollars?')
convert_rate = float(input('CONVERSION_FACTOR>'))
print('What is the cost of the item you would like to purchase?')
item_cost = float(input('PRICE>'))
dollars = float(item_cost * convert_rate)
print('The item that costs', item_cost, 'in', currency, 'costs $', round(dollars, 2), 'in US dollars.')
print('OUTPUT', round(dollars, 2))
