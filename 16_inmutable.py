items = [
	{'product': 'camisa', 
	 'price': 100,
	},
	
	{'product': 'pantalones',
	 'price': 300
	},
	
	{'product': 'Pantalones 2',
	 'price': 200
	},
]


def add_taxes(item):
	new_item = item.copy()
	new_item['taxes'] = item['price'] * .19
	return item
		
new_items = list(map(add_taxes, items))
print('New list')
print(new_items)
print('Old list')
print(items)