from flask import request, jsonify, Blueprint, abort
from Src.View.Landing import Landing

transaction = Blueprint('transaction', __name__)


@transaction.route('/api/v1', methods=['GET'])
def index():
    return jsonify(Landing.view())
