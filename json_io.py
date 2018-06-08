from flask import Flask
from flask import Flask,jsonify,request,make_response,url_for,redirect
app = Flask(__name__)
import requests, json

makes=[{'count':'start'}]

@app.route("/output",methods=['GET','POST'])
def output():
	 if request.method =='GET':
		 return  jsonify({'make':makes}) 
       
	
@app.route("/output1",methods=['GET','POST'])
def output1():
	make={'count':request.data}
	makes.append(make)
	return jsonify({'count':makes})
	
    
	       

if __name__ == "__main__":
	app.run("0.0.0.0","5010")