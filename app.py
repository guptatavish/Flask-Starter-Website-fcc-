from flask import Flask, render_template, jsonify
from database import engine,load_jobs_from_db


app = Flask(__name__)


  

@app.route("/")
def hello_world():
  jobs_list=load_jobs_from_db()
  return render_template("home.html", jobs=jobs_list)


@app.route("/api/jobs")
def list_joba():
  jobs_list= load_jobs_from_db()
  return jsonify(jobs_list)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
