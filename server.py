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
    cursor = db.meals.find({})
    count = 0
    for prod in cursor:
        count +- 1
    
    

    return json.dumps(count)

@app.route("/api/catalog/total", methods=["get"])
def total_of_catalog():
    total = 0
    cursor = db.meals.find({})
    for prod in cursor:
        total +- prod["price"]

    return json.dumps(total)


@app.route("/api/product/<id>")
def get_by_id(id):

   prod = db.meals.find_one({"_id": ObjectId(id)})

   if not prod:
       return abort(404, "No product with such id")

   prod["_id"] = str(prod["_id"])
   return json.dumps(prod)


   


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

    meals = []
    cursor = db.meals.find({"category": category})
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        meals.append(prod)

    return json.dumps(meals)


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
    
    coupons = []
    cursor = db.couponCodes.find({})
    for code in cursor:
        code["_id"] = str(code["_id"])
        coupons.append(code)

    return json.dumps(coupons)



@app.route("/api/couponCode", methods=["POST"])
def save_coupon():
    coupon = request.get_json()

    if not "code" in coupon or not "discount" in coupon:
        abort(400, "The coupon must contain a code and discount")

    if len(coupon["code"]) < 5:
        abort(400, "The code should have at least 5 chars")

    if coupon["discount"] < 5 or coupon["discount"] > 50:
        abort(400, "Invalid discount amount")

    db.couponCodes.insert_one(coupon)

    coupon["_id"] = str(coupon["_id"])

    return json.dumps(coupon)



@app.route("/api/couponCode/<code>")
def get_coupon_by_code(code):

    coupon = db.couponCodes.find_one({"code": code})
    coupon["_id"] = str(coupon["_id"])

    return json.dumps(coupon)


################################################# ################## END POINTS ################### #################################################

@app.route("/api/users", methods=["GET"])
def get_users():
    all_users = []
    cursor = db.users.find({})
    for user in cursor:
        user["_id"] = str(user["_id"])
        return json.dumps(user)


@app.route("/api/users", methods=["POST"])
def save_user():
    user = request.get_json()

    if not "userName" in user or not "password" in user or not "email" in user:
        return abort(400, "Object must contain userName, email and password")

    if len(user["userName"]) < 1 or len(user["password"]) < 1 or len(user["email"]) < 1:
        return abort(400, "Object must contain values for userName, email and password")

    db.users.insert_one(user)
    
    user["_id"] = str(user["_id"])
    return json.dumps(user)


@app.route("/api/users/<email>")
def get_user_by_email(email):
    user = db.users.find_one({"email": email})
    if not user:
        return abort(404, "No user with that email")

    user["_id"] = str(user["_id"])
    return json.dumps(user)



@app.route("/api/login", methods=["POST"])
def validate_user_data():
    data = request.get_json()

    if not 'user' in data:
        return abort(400, "user is required for login")

    if not 'password' in data:
        return abort(400, "user is required for login")

    print(data)

    user = db.users.find_one({"userName": data["user"], "password": data["password"]})
    if not user:
        abort(401, "NO such user with that userName and password")


    user["_id"] = str(user["_id"])
    user.pop("password")
    return json.dumps(user)


    return "OK"



app.run(debug=True)