


def test_dict():
    me = {
        "first": "Aaron",
        "last": "Erebholo",
        "age": 35,
        "hobbies": [],
        "address": {
            "street": "Montezuma",
            "city": "San Diego"
        }
    }


    print(me["first"] + " " + me["last"])

    print("My age is: " + str(me["age"]))
    print(f"My age is: {me['age']}")

    address = me["address"]
    print(type(address))
    print(address)
    print(address["street"])

    print(me["address"]["city"])

    me["color"] = "red"

    me["age"] = 36

    if "age" in me:
        print("Age exist")


print("----- Dictionary Test -------")
test_dict()