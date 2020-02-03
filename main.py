from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "diar"


@app.route("/webhook", methods=["GET", "POST"])
def tracking():
    """Endpoint for receiving webhook from bitbucket."""
    if request.method == "POST":
        data = request.get_json()
        print data["webhookEvent"]
        return "OK"
    else:
        pprint(vars(request))
        return "Webhoook"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)