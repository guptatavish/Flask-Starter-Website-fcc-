from flask import Flask, render_template, jsonify
from database

app = Flask(__name__)
JOBS = [
    {
        'id': 1,
        'title': 'Content Writer',
        'location': 'On Campus',
        'salary': 4000,
    },
    {
        'id': 2,
        'title': 'Publicity',
        'location': 'On Campus',
        'salary': 4300,
    },
    {
        'id': 3,
        'title': 'Backend Engineer',
        'location': 'Remote',
        'salary': 5000,
    },
    {
        'id': 4,
        'title': 'Manager',
        'location': 'On Campus',
        'salary': 4800,
    },
]

def load_jobs_from_db():
  with engine.connect() as conn:
  alldatalist=[]
  tableheads=['id','title','location','salary','currency','resbi','requi']
  result=conn.execute(text("select * from jobs"))
  results_dict=[]
  for row in result.all():
    l1=[]
    l1.append(row)
    a1=zip(tableheads,l1)
    

  print(results_dict)
  

@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_joba():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
