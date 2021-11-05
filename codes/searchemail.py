from elasticsearch import Elasticsearch

def checkemailexists(email):
    es = Elasticsearch()
    e2 ={
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "email_id.keyword" : email,
                                
                                }
                        }
                        ]
                        }
                    }
                }
    resp = es.search(index = 'emps', body = e2)
    print("Data searching")
    hits = resp["hits"]["hits"]
    if hits:
        # error = "Email/Phone already registered"
        # return render_template('signup.html', error = error)
        return True
    else:
       return False