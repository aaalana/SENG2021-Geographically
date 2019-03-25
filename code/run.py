from flask import Flask

app = Flask(__name__)

@app.route('/')
def test_page():
    return "Now we just need the whole finished project (Geographically) to put on the server..."

if __name__ == '__main__':
    app.run()
