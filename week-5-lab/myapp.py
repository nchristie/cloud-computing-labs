from flask import Flask, jsonify

all_records = [
    {
        "name": "Radiohead",
        "albums": [
            {
                "title": "The King of Limbs",
                "songs": [],
                "description":"..."
            },
            {
                "title": "OK Computer",
                "songs": [],
                "description":"..."
            }
        ]
    },
    {
        "name": "Portishead",
        "albums": [
            {
                "title": "Dummy",
                "songs": [],
                "description":"..."
            },
            {

                "title": "Third",
                "songs": [],
                "description":"..."
            }
        ]
    }
]

app = Flask(__name__)


@app.route('/')
def hello():
    return('<h1>Hello World!</h1>')


@app.route('/records/', methods=['GET'])
def get_records():
    return jsonify(all_records)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
