from flask import Flask
# from housing.logger import logging

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    # logging.info("we are testing logging module")
    return "ci cd pipeline has been established, done, ok, final, now its done"

if __name__ == ('__main__'):
        app.run(debug=True)

