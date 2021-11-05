from flask import Blueprint
from codes.signup import signups
from codes.signin import index
from codes.profile import profiles
from codes.signout import dropsessions
from codes.forgetpassword import forgetpasswords
from codes.updatenumber import updatenumbers
from flask import Flask
from elasticsearch import Elasticsearch
import os
import logging, sys

second = Blueprint("second", __name__, codes_folder = "codes", templates_folder = "templates")
logging.basicConfig(filename='record.log', level=logging.DEBUG)
logger = logging.getLogger()
sys.stderr.write = logger.error
sys.stdout.write = logger.info

@second.route('/', methods = ['GET', 'POST'])
def signin():
    return index()


@second.route('/profile', methods=["POST", "GET"])
def profile():
    return profiles()

@second.route('/signup', methods = ['POST', 'GET'])
def signup():
    return signups()

@second.route('/forgetpassword', methods = ['POST', 'GET'])
def forgetpassword():
    return forgetpasswords()


@second.route('/dropsession', methods=["POST", "GET"])
def dropsession():
    return dropsessions()

@second.route('/updatenumber', methods=["POST", "GET"])
def updatenumber():
    return updatenumbers()
    
    
#@second.route('/updatepassword', methods=["POST", "GET"])
#def updatepassword():
#    return updatepass()