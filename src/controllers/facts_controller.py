# from bson import ObjectId
from flask import Blueprint, jsonify
# from flask import Blueprint, jsonify, request
from models.facts_model import FactsModel
from utils.http_status import HttpStatus


facts_controller = Blueprint("facts", __name__)


def _get_all_facts():
    facts = FactsModel.find()
    return [fact.to_dict() for fact in facts]


@facts_controller.route("/", methods=["GET"])
def facts_index():
    facts_list = _get_all_facts()
    return jsonify(facts_list), HttpStatus.OK.value


# def _get_fact(id: str):
#     return FactsModel.find_one({"_id": ObjectId(id)})

# @facts_controller.route("/random", methods=["GET"])
# def fact_random():
#     fact = FactsModel.get_random()
#     if fact is None:
#         return jsonify({"error": "No musics available"}), HttpStatus.NOT_FOUND

#     return jsonify(fact.to_dict()), HttpStatus.OK


# @music_controller.route("/", methods=["POST"])
# def music_post():
#     new_music = MusicModel(request.json)
#     new_music.save()
#     return jsonify(new_music.to_dict()), HttpStatus.CREATED


# @music_controller.route("/<id>", methods=["GET"])
# def music_show(id: str):
#     music = _get_music(id)
#     if music is None:
#         return jsonify({"error": "Music not found"}), HttpStatus.NOT_FOUND
#     return jsonify(music.to_dict()), HttpStatus.OK
