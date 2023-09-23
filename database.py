from sqlalchemy import create_engine,text

engine=create_engine("mysql+pymysql://6dsll2jfineiqjwaj4qg:pscale_pw_f5qefCnmmRBqowQE3e5swWj0LddQ8oizZReUUuOBNF1@aws.connect.psdb.cloud/mockweb1?charset=utf8mb4",connect_args={
  "ssl": {
    "ssl_ca":"etc/ssl/cert.pem"
  }
})


def load_jobs_from_db():
  with engine.connect() as conn:
    alldatalist=[]
    tableheads=['id','title','location','salary','currency','resbi','requi']
    result=conn.execute(text("select * from jobs"))
    for row1 in result.all():
      l1=[]
      for i in row1:
        l1.append(i)
      a1=[]
      a1=zip(tableheads,l1)
      alldatalist.append(dict(a1))
  return alldatalist