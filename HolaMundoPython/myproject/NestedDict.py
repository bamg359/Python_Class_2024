
products={
    "prod1":{
        "Name: ": "Café JuanVal",
        "Price:": 23000,
        "Cost: ": 19000,
        "Quantity": 100,
        "Category:": "granes",
        "subcategory: ": "Beverage"
    },

    "prod2":{
        "Name: ": "Sugar Manuelita",
        "Price:": 2600,
        "Cost: ": 2400,
        "Quantity": 100,
        "Category:": "granes",
        "subcategory: ": "market"
    }
}

print(products["prod1"]["Price:"])


for j,k in products.items():
    print(j,k)



prod3 ={
        "Name:": "Penela",
        "Price:": 4900,
        "Cost:": 4300,
        "Quantity": 100,
        "Category:": "granes",
        "subcategory: ": "market"
    }

products.update({"prod3": prod3})

for j,k in products.items():
    print(j,k)




