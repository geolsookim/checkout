import requests


def checkout(url, items):
    """
    Args:
        url (string): url of price service
        items (list): List of strings, each string representing an item or a bundle of items

    Returns:
        int: total price of items 

    >>> checkout(' https://api.myjson.com/bins/gx6vz', ['A'])
    20

    >>> checkout(' https://api.myjson.com/bins/gx6vz', ['A*'])
    50

    >>> checkout(' https://api.myjson.com/bins/gx6vz', ['A', 'A*'])
    70

    >>> checkout(' https://api.myjson.com/bins/gx6vz', ['A', 'A', 'A', 'A'])
    80

    >>> checkout(' https://api.myjson.com/bins/gx6vz', ['A', 'A', 'D*'])
    130

    >>> checkout(' https://api.myjson.com/bins/gx6vz', [])
    0

    >>> checkout(' https://api.myjson.com/bins/gx6vz', ['XYZ'])
    0
    """

    try:
        resp = requests.get(url)    
    except request.exceptions.ConnectionError:
        return -1

    if resp.status_code != 200:
        return -1

    try:
        price_list = resp.json().get('prices')
    except (ValueError, AttributeError):
        return -1

    if not price_list:
        return -1

    unit_prices = {item.get('name') : item.get('unit_price') for item in price_list}

    special_prices = {item.get('name')+'*' : item.get('special_price') for item in price_list if 'special_price' in item}

    all_prices = {**unit_prices, **special_prices}

    total = 0
    for item in items:
        total += all_prices.get(item, 0)
        
    return total
