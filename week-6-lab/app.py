from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  html = f"<h1>Hello!</h1>"
  return html

@app.route("/<name>/", methods=['GET'])
def get_hello(name):
  html = f"<h1>Hello {name}!</h1>"
  return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)