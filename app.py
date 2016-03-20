from flask import Flask, render_template, request, jsonify, Response, json

app = Flask(__name__)

@app.route('/')                                 #by default this can  handle only GET methods, we need to declare POST if we need (form submissions)
def index():
	return render_template('index.html')

@app.route('/about/')
def about():
    return 'A Project by ISTE- NITK Chapter.'

@app.route('/login/')
def login():
	return render_template('my-form.html')

@app.route('/login/', methods=['POST'])
def login_post():

    text = request.form['apptext']      #this should match the name in the html template (which it does)
    processed_text = text.upper()
    return processed_text

    '''
    if request.method == 'POST':
    	return 'You are using POST'
    else:
    	return 'Probably GET'
    '''

@app.route('/apprec/<value>')                                           
def apprec(value):
    #return render_template('app-rec.html',value=value)  # see split method
    #value is of format: Host$Value1$Value2$Value3
    #extract host no, store values as H1= {val1, val2, val3} and so on for all hosts, each host being a list (array)
    H1 = value.split("$") 
    return Response(json.dumps(H1),  mimetype='application/json')
    #this stores H1 as a list of host, val1, val2 and val3

    


#******************IMPORTANT**************
#This is a new route. If this webpage notices HTTP post, it will just echo what was sent through this protocol (from app)
#HttpPost httpPost = new HttpPost("url");
#This should work. Basically you create a http post object and send it to that url. if you keep 
#refreshing the call to the HTTPpost then it ought to work dynamically

@app.route("/data", method=("POST",))
def handle_data():
    return "You sent me " + str(request.values)     #This will get the data from the app as soon as it sees app has sent HTTP post request

#try and receive the data in a round robin data structure (constant time for all hosts), serialize, and send to the triangulation part

@app.route('/json')  #jsonify can be used on a dictionary to give list as JSON objects: import jsonify and return jsonify(results=list)
def test_json():
    list = [
            {'a': 1, 'b': 2},
            {'a': 5, 'b': 10}
           ]
    return Response(json.dumps(list),  mimetype='application/json') #Import Response and json and use json.dumps to return as simpler list

#Considering another example for jsonifying some data: 
  

@app.route('/profile/<name>/')							#name is the variable we pass to this route 
def hello(name):
	return render_template('page.html', name=name) 		#the first name is a keyword, second is the variable in page.html	THIS IMPLEMENTS GET

if __name__ == '__main__':
	app.run(debug=True, host= '0.0.0.0', port=int("8000"))



	'''
	@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

    '''