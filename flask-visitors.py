# import flask module
from flask import Flask

# instance of flask application
app = Flask(__name__)
#vars
visits = 0

# home route that returns below text when root url is accessed
@app.route("/metrics")
def fuckinmetric():
    global visits
    visits +=1
    return '{}'.format(visits)

if __name__ == '__main__':  
   app.run()