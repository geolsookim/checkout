# checkout(url, items)

checkout(url, items) is a function that takes two arguments and returns an integer

The two arguments are:

- url (string): url of json service which returns pricing rule
- items (list): list of strings representing items and bundles of items

The returned integer is the total price of the list of items


## Requirements

- Python 3

- requests==2.13.0


## Assumptions

The 'items' argument is a list of strings, each string representing an item or a bundle of n items, where n is the item's special quantity value

The string representing an item is the name of the item in the returned pricing rule

The string representing a bundle of items is the name of the item suffixed with '*'

So for example, if 'https://price_url.com/' is a json service that returns the following pricing rule:

```json
{
	"prices": [{
		"name": "A",
		"unit_price": 20,
		"special_qty": 3,
		"special_price": 50
	}]
}
```

then the string 'A*' represents a bundle of 3 'A' items, and a call to the function

```python
checkout('https://price_url.com', ['A', 'A*'])
```

will return the integer 70
