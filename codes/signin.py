from flask import Flask, render_template, url_for, request, redirect, session, flash
from elasticsearch import Elasticsearch
import re
from codes.searchemailandpassword import emailandpasswordexists
from codes.searchphoneandpasswordexists import phoneandpasswordexists


es = Elasticsearch()


def index():
    error = None
    session.pop('user', None)
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        print("data reading")
        print("Data searching")
        
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        if(re.match(regex, email)):
            email = email
            source = emailandpasswordexists(email, password)
            if source is not None :
                print("Its printing from line num 27", source)
                return render_template('profile.html', output_source = source)
            else:
                print("Email printed")
                error = "invalid input"
                return render_template('login.html', error = error)
        
        elif re.findall('[7-9][0-9]{9}', email):
            phone = email
            phone_source = phoneandpasswordexists(phone, password)
            if phone_source is not None:
                print("Its printing from line num 38", phone_source)
                return render_template('profiles.html', output_phone = phone_source)
            else:
                print("phone printed")
                error = "invalid input"
                return render_template('login.html', error = error)
        else:
            error = "Invalid Input"
            return render_template('login.html', error = error)