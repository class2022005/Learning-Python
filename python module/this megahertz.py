#!/usr/bin/env python3
# Given a dictionary (catalog) whose keys are product names and values are product prices per unit and a list of tuples (order) of 
# product names and quantities, compute and return the total value of the order.
# Example catalog:
# {
# 'AMD Ryzen 5 5600X': 289.99,
# 'Intel Core i9-9900K': 363.50,
# 'AMD Ryzen 9 5900X': 569.99
# }
# Example order:
# [
# ('AMD Ryzen 5 5600X', 5), 
# ('Intel Core i9-9900K', 3)
# ]
# Example result:
# 2540.45
# How the above result was computed:
# (289.99 * 5) + (363.50 * 3)
def q6(catalog, order):
    res = 0
    for name, number in order:
        res += number * catalog[name]
    # for index, name in enumerate(catalog):
    #     if name[0] == order[index]:
    #         res += order[index[1]]
    # print(res)
    return res

catalog = {
'AMD Ryzen 5 5600X': 289.99,
'Intel Core i9-9900K': 363.50,
'AMD Ryzen 9 5900X': 569.99
}

order = [
('AMD Ryzen 5 5600X', 5), 
('Intel Core i9-9900K', 3)
]

q6(catalog,order)