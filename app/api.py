from app import app, db
from flask import request, jsonify
from models import Item, Category
from collections import defaultdict


@app.route("/components/all", methods=["GET"])
def allTools():
    categories = {category.id: category.name for category in Category.query.all()}
    val = defaultdict(lambda: [])
    for item in Item.query.all():
        item_cat = categories[item.category]
        val[item_cat].append("TEMP") # GET LIST OF ARGS
    return jsonify(val)