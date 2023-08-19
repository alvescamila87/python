from bottle import route, run

@route('/')
def index():
    return ("<h1>Hello guys!</h1>")

if __name__ == '__main__':
    run()
