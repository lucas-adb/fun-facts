from bson import ObjectId
from flask import Blueprint, jsonify, request
from models.facts_model import FactsModel
from utils.http_status import HttpStatus


facts_controller = Blueprint("facts", __name__)


# Gets all facts:
def _get_all_facts():
    facts = FactsModel.find()
    return [fact.to_dict() for fact in facts]


@facts_controller.route("/", methods=["GET"])
def facts_index():
    facts_list = _get_all_facts()
    return jsonify(facts_list), HttpStatus.OK.value


# Get a fact by its id:
def _get_fact(id: str):
    return FactsModel.find_one({"_id": ObjectId(id)})


@facts_controller.route("/<id>", methods=["GET"])
def fact_show(id: str):
    fact = _get_fact(id)
    if fact is None:
        return jsonify({"error": "Fact not found"}), HttpStatus.NOT_FOUND.value
    return jsonify(fact.to_dict()), HttpStatus.OK.value


# Get a random fact:
@facts_controller.route("/random", methods=["GET"])
def fact_random():
    fact = FactsModel.get_random()
    if fact is None:
        return (
            jsonify({"error": "No facts available"}),
            HttpStatus.NOT_FOUND.value
            )

    return jsonify(fact.to_dict()), HttpStatus.OK.value


# Create a new fact:
@facts_controller.route("/", methods=["POST"])
def fact_post():
    new_fact = FactsModel(request.json)
    new_fact.save()
    return jsonify(new_fact.to_dict()), HttpStatus.CREATED.value
