#!/usr/bin/python
print('hellow,你好')
from flask import Flask, abort, request, jsonify
import random
app = Flask(__name__)

# 测试数据暂时存放
tasks = []

@app.route('/add_task/', methods=['POST'])
def add_task():

    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)

    index = random.randint(1000000,99999999)
    task = {
        'id': request.json['id'],
        'info': request.json['info']
    }
    tasks.append(task)
    print(request.json,request.url)
    return jsonify({'result': 'success',
                    'code':200,
                    'syu':index,
                    "task":task})


@app.route('/get_task/', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        # 没有指定id则返回全部
        print(request.json)
        return jsonify(tasks)
    else:
        task_id = request.args['id']
        task = filter(lambda t: t['id'] == int(task_id), tasks)
        return jsonify(task) if task else jsonify({'result': 'not found'})


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=8383, debug=True)
