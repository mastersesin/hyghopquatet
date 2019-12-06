from flask import request, jsonify, Blueprint, abort
from Src.View.Landing import Landing
from Src.View.Order import Order

transaction = Blueprint('transaction', __name__)


@transaction.route('/api/v1', methods=['GET'])
def index():
    return jsonify(Landing.view())


@transaction.route('/api/v1/order', methods=['POST'])
def order():
    if request.is_json:
        # name = request.json.get('name', None)
        # congty = request.json.get('congty', None)
        # email = request.json.get('email', None)
        # dienthoai = request.json.get('dienthoai', None)
        # diachi = request.json.get('diachi', None)
        # soluong = request.json.get('soluong', None)
        # ngaycanhang = request.json.get('ngaycanhang', None)
        # ghichukhac = request.json.get('ghichukhac', None)
        # params = [name, congty, email, dienthoai, diachi, soluong, ngaycanhang, ghichukhac]
        params = request.json.get('params', None)
        if params:
            Order.view(params=params)
            return jsonify({'code': 1, 'msg': 'Đặt hàng thành công'})
        else:
            return jsonify({'code': 0, 'msg': 'Invalid request.'})
    else:
        return jsonify({'code': 0, 'msg': 'Invalid request.'})
