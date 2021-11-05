from elasticsearch import Elasticsearch

def checkenumberexists(Phone):
    es = Elasticsearch()
    e2 ={
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "Phone.keyword" : Phone,
                                
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