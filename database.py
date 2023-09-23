from sqlalchemy import create_engine,text

engine=create_engine("mysql+pymysql://6dsll2jfineiqjwaj4qg:pscale_pw_f5qefCnmmRBqowQE3e5swWj0LddQ8oizZReUUuOBNF1@aws.connect.psdb.cloud/mockweb1?charset=utf8mb4",connect_args={
  "ssl": {
    "ssl_ca":"etc/ssl/cert.pem"
  }
})


    
