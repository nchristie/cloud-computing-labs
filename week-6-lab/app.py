from flask import Flask

app = Flask(__name__)

names = ['Arman', 'Naomi']

@app.route("/")
def hello():
  html = "<h1>Hello {name}!</h1>".format(name="Arman")
  return html

@app.route("/names/<name>", methods=['GET'])
def get_hello(name):
  html = f"<h1>Hello {name}!</h1>"
  return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)