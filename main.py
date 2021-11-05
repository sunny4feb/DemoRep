from codes.signup import signups
from codes.signin import index
from codes.profile import profiles
from codes.signout import dropsessions
from codes.forgetpassword import forgetpasswords
from codes.updatenumber import updatenumbers
from codes.updatepassword import updatepasswords
from flask import Flask, flash
from elasticsearch import Elasticsearch
import os
import logging, sys





es = Elasticsearch()
app = Flask(__name__)



app.secret_key = os.urandom(4)



logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f' %(levelname)s %(name)s %(threadName)s %(pathname)s %(lineno)d: %(message)s')
logging.basicConfig(filename='record.log', level=logging.DEBUG)
logger = logging.getLogger()
# sys.stderr.write = logger.error
sys.stdout.write = logger.info

@app.route('/', methods = ['GET', 'POST'])
def signin():
    return index()


@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    return profiles()

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    return signups()

@app.route('/forgetpassword', methods = ['GET', 'POST'])
def forgetpassword():
    return forgetpasswords()


@app.route('/dropsession', methods = ['GET', 'POST'])
def dropsession():
    return dropsessions()

@app.route('/updatenumber', methods = ['GET', 'POST'])
def updatenumber():
    return updatenumbers()
    
    
@app.route('/updatepassword', methods=["POST", "GET"])
def updatepassword():
    return updatepasswords()
if __name__ == '__main__':
    app.run('localhost',5050, debug=True)