def calculate_total(items_purchased, grocery_list):
    item_prices = {
        "milk": 2.50,
        "eggs": 3.25,
        "bread": 1.21,
        "cheese": 3.50,
        "apples": 7.44,
        "bananas": 3.88,
        "carrots": 3.89,
        "lettuce": 1.12,
        "potatoes": 32.21,
        "cereal": 5.99,
    }

    unpurchased_items = []
    receipt = {}

    for item in items_purchased:
        if item in item_prices:
            receipt[item] = item_prices[item]
        
    for item in grocery_list:
        if item not in items_purchased:
            unpurchased_items.append(item)

    total = sum(receipt.values())

    return unpurchased_items, receipt, total
