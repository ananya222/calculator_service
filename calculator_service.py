from flask import Flask,request
app=Flask(__name__)
import bodmas as bm

@app.route("/api/add/",methods=['GET'])
def add():
    num=request.args.to_dict()
    sum=0
    for _,v in num.items():
        sum+=float(v)
    return str(sum)

@app.route("/api/subtract/",methods=['GET'])
def subtract():
    num=request.args.to_dict()
    diff=float(num['a'])+float(num['a'])
    for _,v in num.items():
        diff-=float(v)
    return str(diff)

@app.route("/api/multiply/",methods=['GET'])
def multiply():
    num=request.args.to_dict()
    prod=1
    for _,v in num.items():
        prod*=float(v)
    return str(prod)

@app.route("/api/divide/",methods=['GET'])
def divide():
    num=request.args.to_dict()
    quot=float(num['a'])*float(num['a'])
    for _,v in num.items():
        quot/=float(v)
    return str(quot)

@app.route("/api/evaluate/",methods=['GET'])
def evaluate():
    exp=request.args.to_dict()
    exp_req=exp['e']
    exp_req=exp_req.replace('a','+')
    exp_req=exp_req.replace('s','-')
    exp_req=exp_req.replace('m','*')
    exp_req=exp_req.replace('d','/')
    exp_req=exp_req.replace('e','=')
    print(exp_req)
    result=bm.parse_expression(exp_req)
    return str(result)

if (__name__=='__main__'):
    app.run(debug=True)
