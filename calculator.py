from flask.json import jsonify
from flask import Flask,request,app
from flask import Flask,request

def sum(number1,number2):
    result= number1+number2
    return result

def sub(number1,number2):
    result= number1-number2
    return result
def mul(number1,number2):
    result= number1*number2
    return result

def div(number1,number2):
    result= number1/number2
    return result

app=Flask(__name__)
@app.route('/sum',methods=['POST','GET'])
def main():

    number1=int(request.form.get('number'))
    number2=int(request.form.get('number'))
    result=sum(number1,number2)
    return jsonify(result)

@app.route('/sub',methods=['POST','GET'])
def hello():
    number1=int(request.form.get('number'))
    number2=int(request.form.get('number'))
    result=sub(number1,number2)
    return jsonify(result)

@app.route('/mul',methods=['POST','GET'])
def how():
    number1=int(request.form.get('number'))
    number2=int(request.form.get('number'))
    result=mul(number1,number2)
    return jsonify(result)

@app.route('/sum',methods=['POST','GET'])
def are():
    number1=int(request.form.get('number'))
    number2=int(request.form.get('number'))
    result=div(number1,number2)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
