from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import json

app = Flask('__name__')

client = MongoClient("mongodb+srv://Ammar:jjFwsqtLhsDhjlFL@cluster0.u0dd9yn.mongodb.net/?retryWrites=true&w=majority")
db = client['company']
collection = db['login_users']

# نقطة النهاية لجلب كل العناصر
@app.route('/home', methods=['GET'])
def get_items():
    items = list(collection.find())
    for item in items:
        item['_id'] = str(item['_id'])  # تحويل ObjectId إلى سلسلة نصية للتعامل مع JSON
    return jsonify(items)



# نقطة النهاية لإضافة عنصر جديد
@app.route('/home', methods=['POST'])
def add_item():
    data = request.json
    result = collection.insert_one(data)
    return {'id': str(result.inserted_id)}, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7575,debug=True)
