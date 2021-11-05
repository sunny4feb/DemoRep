from flask import Flask, render_template, session
from elasticsearch import Elasticsearch
from codes.signin import *
from codes.searchemailandpassword import emailandpasswordexists


def profiles():
    session.pop('user', None)
    #Username = session['user']
    #data = index.signinname
    print("Printing profile")
    # empwd = emailandpasswordexists(email, password)
    # hits = empwd['hits']['hits']
    # for hit in hits:
    #     source = hit['_source']
    #     name = source['Username']
    #     print(name)

    return render_template('profile.html')
    
    

    # source['Username']