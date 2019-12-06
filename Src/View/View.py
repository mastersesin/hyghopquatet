from flask import request, jsonify, Blueprint, abort
from Src.View.Landing import Landing
from Src.View.Order import Order

transaction = Blueprint('transaction', __name__)


@transaction.route('/api/v1', methods=['GET'])
def index():
    return jsonify(Landing.view())


@transaction.route('api/v1/order', methods=['POST'])
def order():
    if request.is_json:
        params = request.json.get('params', None)
        if params:
            return jsonify(Order.view(params=params))
        else:
            return jsonify({'code': 0, 'msg': 'Invalid request.'})
    else:
        return jsonify({'code': 0, 'msg': 'Invalid request.'})
