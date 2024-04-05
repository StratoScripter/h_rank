'''
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.
'''

from collections import OrderedDict
items = int(input())
shopping_dict = OrderedDict()
for _ in range(items):
    input_items = input()
    item_name, net_price = input_items.rsplit(' ', 1)
    net_price = int(net_price)
    if item_name not in shopping_dict:
         shopping_dict[item_name] = net_price
    else:
        shopping_dict[item_name] += net_price
for item_name, net_price in shopping_dict.items():
    print(f'{item_name} {net_price}')