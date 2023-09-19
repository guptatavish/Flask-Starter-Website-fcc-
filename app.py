from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
  return "If you are reading this then you must be Bala, I hope you have a good night !"

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)