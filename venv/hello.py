from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print('장경희 바보')
    return "Hello World!"

if __name__ == "__main__":
    app.run()