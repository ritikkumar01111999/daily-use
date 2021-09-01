from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route("/api/add",method=['GET'])
def add():
    """This is a function to recive values from requestobject
    complete the calculation 
    format the result into jason 
    return the json response object""""


    number1=request.args.get("enter the first number",type=int)
    number2=request.args.get("enter the second number",type=int)
    total=number1+number2
    response=make_response(
        jsonify({"result":str(total)}),

    

    )
    response.headers["content-Type"]="application/json"
    #return response
    return
@app.route("/api/sub",method=['GET'])
def sub():
    """This is a function to recive values from requestobject
    complete the calculation 
    format the result into jason 
    return the json response object""""

    number1=request.args.get("enter the first number",type=int)
    number2=request.args.get("enter the second number",type=int)
    total=number1-number2
    response=make_response(
        jsonify({"result":str(total)}),

    

    )
    response.headers["content-Type"]="application/json"
    #return response
    return
@app.route("/api/mul",method=['GET'])
def mul():
    """This is a function to recive values from requestobject
    complete the calculation 
    format the result into jason 
    return the json response object""""

    number1=request.args.get("enter the first number",type=int)
    number2=request.args.get("enter the second number",type=int)
    total=number1*number2
    response=make_response(
        jsonify({"result":str(total)}),

    

    )
    response.headers["content-Type"]="application/json"
    #return response
    return
@app.route("/api/DIV",method=['GET'])
def div():
    """This is a function to recive values from requestobject
    complete the calculation 
    format the result into jason 
    return the json response object""""

    number1=request.args.get("enter the first number",type=int)
    number2=request.args.get("enter the second number",type=int)
    total=number1/number2
    response=make_response(
        jsonify({"result":str(total)}),

    

    )
    response.headers["content-Type"]="application/json"
    #return response
    return
