import json
from flask import Flask, abort, request
from mock_data import catalog
from config import db
from bson import ObjectId


app = Flask("Server")



@app.route("/")
def home():
    return "Hello from Flask"


@app.route("/me")
def about_me():
    return "Aaron Erebholo"

#############################
####### API ENDPOINTS #######
#############################


@app.route("/api/catalog", methods=["get"])
def get_catalog():

    meals = []
    cursor = db.meals.find({})

    for prod in cursor:
        prod["_id"]  = str(prod["_id"])
        meals.append(prod)

    return json.dumps(meals)

@app.route("/api/catalog", methods=["post"])
def save_product():
    # set an unique _id on
    product = request.get_json()

    db.meals.insert_one(product)
    print(product)

    product["_id"] = str(product["_id"])
   
    return json.dumps(product)
    


@app.route("/api/catalog/count", methods=["get"])
def product_count():
    count = len(catalog)
    return json.dumps(count)

@app.route("/api/catalog/total", methods=["get"])
def total_of_catalog():
    total = 0
    for prod in catalog:
        total +- prod["price"]

    return json.dumps(total)


@app.route("/api/product/<id>")
def get_by_id(id):

    for prod in catalog:
        if prod["_id"] == id:
            return json.dumps(prod)


    return abort(404, "ae0001")


@app.route("/api/product/cheapest")
def cheapest_product():

    solution = catalog[0]
    for prod in catalog:
        if prod["price"] < solution["price"]:
            solution = prod

    return json.dumps(solution)



@app.get("/api/categories")
def unique_categories():

    categories = []
    for prod in catalog:
        category = prod["category"]

        if not category in categories:
            categories.append(category)

    return json.dumps(categories)


@app.get("/api/catalog/<category>")
def prods_bycategory(category):
    result = []
    for prod in catalog:
        if prod["category"] == category:
            result.append(prod)



    
    return json.dumps(result)


# Practice
@app.get("/api/someNumbers")
def some_numbers():
    numbers = []
    for num in range(1, 51):
        numbers.append(num)

    return json.dumps(numbers)


#######################################
######## Coupon Code EndPoints ########
#######################################

allCoupons = []

@app.route("/api/couponCode", methods=["GET"])
def get_coupon():
    return json.dumps(allCoupons)



@app.route("/api/couponCode", methods=["POST"])
def save_coupon():
    coupon = request.get_json()
    coupon["_id"] = 42

    allCoupons.append(coupon)

    return json.dumps(coupon)







app.run(debug=True)