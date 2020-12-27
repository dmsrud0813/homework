from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    orderer_receive = request.form['orderName_give']
    postcode_receive = request.form['postcode_give']
    adress_recieve = request.form['adress_give']
    orderQuantity_receive = request.form['orderQuantity_give']
    mobileNum_receive = request.form['mobileNum_give']

    orderInfo = {
        'orderer': orderer_receive,
        'postcode': postcode_receive,
        'adress': adress_recieve,
        'orderQuantity': orderQuantity_receive,
        'mobileNum': mobileNum_receive,

    }
    db.orderInfos.insert_one(orderInfo)
    return jsonify({'result': 'success', 'msg': '저장 성'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.orderInfos.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
