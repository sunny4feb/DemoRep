from flask import Flask, render_template, request
from elasticsearch import Elasticsearch


def forgetpasswords():
    if request.method == 'GET':
        return render_template('forgetpassword.html')
    else:
        pass