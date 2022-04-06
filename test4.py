from mock_data import catalog


def find_prod():
    text = "Plate"


    for prod in catalog:
        title = prod["title"]
        print(title)
        if text.lower() in title.lower():
            print(f"{title} ${prod['price']}")

    
def unique_categories():
    categories = []
    for prod in catalog:
        category = prod["category"]

        if not category in categories:
            categories.append(category)


    print(categories)



find_prod()
unique_categories()