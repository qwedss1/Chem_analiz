import json
import os
def dict_formation():
    d=dict()
    d1=dict()
    d2=dict()
    with open('cashew.json') as f:
        d=json.load(f)
    k=0
    for key,value in d.items():
        if k<2 && value!=[]:
            d1[key]=value
        elif value!=[]:
            d2[key]=value
        k++
    d=dict()
    d.update(d1)
    d.update(d2)
    os.remove('cashew.json')
    with open('cashew.json') as f:
        d=json.dump(d,f)              
