from bottle import route, run, request

@route("/")
def index(q=""):
    a = request.query.get("q")
    return "<h1> Input is {name}<h1>".format(name=a)
run(host="0.0.0.0", port=80)