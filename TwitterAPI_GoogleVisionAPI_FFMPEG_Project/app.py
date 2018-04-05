from flask import Flask
from qicode import get_images
from test1 import test1
from test2 import test2
from test3 import test3




app = Flask(__name__)

@app.route('/')
def homepage():
	return  """
<!DOCTYPE html>
<head>
   <title>API Assignment</title>
</head>
<body style="width: 880px; margin: auto;">  
  <style>

  body{

  /* Old browsers */
  background: #141E30;
  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(-45deg, #35577D, #141E30);
  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(-45deg, #35577D, #141E30);
  margin: 0;
  padding: 0;

  }

    h1{
    	color: aliceblue;
        font-size: xx-large;
        font-weight: bold;
        color: blue;
    }
  	.instruction{
  	    color: aliceblue;
  		font-size: x-large;
  		font-family: Arial;
  	}
  </style>
    <h1>Code Review Local Host Website For Qi Wang</h1>
    <p class="instruction">Current location <b>localhost:5000</b></p>
    <p class="instruction">Hi welcome to Boris Huang's local host code review website </p>
    <p class="instruction">For API module output go to <b>/output</b></p>
    <p class="instruction">For Failure Testing (Test 1) go to <b>/test1</b></p>
    <p class="instruction">For Timing Testing (Test 2) go to <b>/test2</b> </p>
    <p class="instruction">For Memory Testing (Test 3) go to <b>/test3<b/> </p>
   
</body>
"""

@app.route("/output")
def output():
	a = get_images('realDonaldTrump')
	return str(a)
	

@app.route("/test1")
def test1():
	a = test1()
	return str(a)

@app.route("/test2")
def test2():
	a = test2()
	return str(a)

@app.route("/test3")
def test3():
	a = test3()
	return str(a)



if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
