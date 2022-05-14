from __future__ import print_function
from flask import *
import sourcecode

app = Flask( __name__ )

@app.route( "/" )
def index():
    return render_template("index.html")

@app.route('/proxynone', methods = ['POST', 'GET'])
def index_proxynone():
    return sourcecode.proxy_none()


if __name__ == "__main__":
    app.run( host = "127.0.0.1", port = 5000 )