import json
from flask import Flask

app = Flask(__name__)


@app.route("/get/info")
def index():
    data = ["武沛齐", "郭智", "住户费"]
    json_string = json.dumps(data, ensure_ascii=False)  # json序列化成JSON格式的字符串

    return json_string


@app.route("/do/play")
def play():
    info = {
        "code": 1000,
        "status": True,
        "values": [
            {"id": 1, "name": "武沛齐"},
            {"id": 2, "name": "陈青"},
            {"id": 3, "name": "梁树彬"},
        ]
    }
    json_string = json.dumps(info, ensure_ascii=False)  # JSON格式的字符串

    return json_string


if __name__ == "__main__":
    app.run()