from flask import Flask, render_template
from country import get_covid_info
import os

app = Flask(__name__)

@app.route('/')
def index():
    obj = get_covid_info()
    return render_template('index.html',data=obj)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
