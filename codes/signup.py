from flask import Flask, render_template, request, flash
from elasticsearch import Elasticsearch
import re
from codes.searchemail import checkemailexists
from codes.searchnumber import checkenumberexists

def signups():
    phone=None
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        #phone = request.form["phone"]
        print("Read the data")
        
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.match(regex, email)):
        #if re.findall("\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email):
            email = email
            my_mail = checkemailexists(email)
            
            phone = None
            print("Email printed")
        elif re.findall('[7-9][0-9]{9}', email):
            phone = email
            my_number =checkenumberexists(phone)
            email = None
            print("phone printed")
        else:
            return "Invalid"

        try:
            es = Elasticsearch()
            e1 ={
            "Username" : name,
            "email_id" : email,
            "password": password,
            "phone" : phone
            }
            es.index(index = "emps", doc_type = 'detail', body = e1)
            print("data inserted")
        except Exception as e:
            pass
        finally:
                return '''Hi {}, You have Successfully signed up !!,
    Please <a href="http://localhost:5050/">click here </a> to LogIn'''.format(name)

    # # emailid = re.findall('\S+@\S+', email)
    # request.form["phone"] == re.findall("(0|91)?[7-9][0-9]{9}"):
    #match2 = re.search(r'^(\d{3}--\d{3}--\d{4})$',email)

    # re.findall('\S+@\S+', s)
    # re.findall('[0-9]+', s) 