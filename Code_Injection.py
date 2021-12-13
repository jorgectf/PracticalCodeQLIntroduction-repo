from flask import Flask, request

app = Flask(__name__)


@app.route("/flow1")
def flow1():
    code = request.args["code"]
    eval(code)


@app.route("/flow2")
def flow2():
    email = request.args["email"]
    eval("./send_email {email}".format(email=email))


def flow3_extra(text):
    return text.split("\n")


@app.route("/flow3")
def flow3():
    text = request.args["text"]
    eval(flow3_extra(text))


@app.route("/flow4")
def flow4():
    text = request.args["text"]
    tixt = text
    toxt = flow3_extra(tixt)
    tuxt = toxt
    eval(tuxt)


@app.route("/flow1_good")
def flow1_good():
    code = request.args["code"]
    if code == "print('Hello, Wo... CodeQL!')":
        eval(code)


# if __name__ == "__main__":
#     app.run(debug=True)
