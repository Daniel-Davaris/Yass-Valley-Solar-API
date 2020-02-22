from app import app, db
from flask import request, jsonify

from models import Item, Category, Customer
from collections import defaultdict


@app.route("/api/components/all", methods=["GET"])
def allTools():
    categories = {category.id: category.name for category in Category.query.all()}
    val = defaultdict(lambda: [])
    for item in Item.query.all():
        item_cat = categories[item.category]
        val[item_cat].append("TEMP") # GET LIST OF ARGS
    return jsonify(val)


@app.route("/api/Customer/new", methods=["POST"])
def newCustomer():
    data = request.get_json()
    c = Customer(**data)

@app.route("/api/quotes/new", methods=["POST"])
def newItem():
    data = request.get_json()
    i = Item(**data)
    