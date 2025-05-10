import pandas as pd
from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine

app=Flask(__name__)

# hugginf face에서 csv 가져옴. fsspec 설치 필요
df = pd.read_csv("hf://datasets/Ammok/apple_stock_price_from_1980-2021/AAPL.csv")

# mysql의 id, 비밀번호, host, port, database를 설정. pymysql 설치 필요
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/stock_info')

# # stock_prices라는 테이블 생성
df.to_sql('stock_prices', con=engine, if_exists='replace', index=False)

# print("안녕하세요")

@app.route("/")
def home():
    return render_template("chart.html")

@app.route("/data")
def get_data():
    df = pd.read_sql("SELECT * FROM stock_prices WHERE Date > '2000-01-01' LIMIT 100", con=engine)
    return jsonify({
        "labels" : df['Date'].tolist(),
        "values" : df['Volume'].tolist()
    })

# run을 하지 않으면 서버가 안열림
# debug -> nodemon처럼 항상 감지 
app.run(debug=True, port=5500)