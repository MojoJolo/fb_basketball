#!flask/bin/python
from app import app
# app.run(host='0.0.0.0',port=4321,debug = True)

if __name__ == "__main__":
    app.run(debug = True)