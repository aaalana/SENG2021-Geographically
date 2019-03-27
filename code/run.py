### Install dependancies/libraries
from flask import Flask

### Set 'flask' environment settings
app = Flask(__name__)

@app.route('/')
def test_page():
    return "Now we just need the whole finished project (Geographically) to put on the server..."

### Start the server, (called through 'serverStart' script)
if __name__ == '__main__':
    app.run()
