from flask import Flask, Response
app = Flask(__name__)

@app.route("/")
def chart():
    with open("chart.html", encoding='utf-8') as f:
        chart_html = f.read()
    return Response(chart_html, mimetype='text/html')

app.run(debug=True)