from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
   #return 'Hello World'
	return render_template('marks.html')

@app.route('/submitform/',methods=['post'])
def submitform():
	result = request.form
	#print(result)
	#return result
	return render_template('result.html',result=result)

@app.route('/second')
def second():
	return render_template('second.html')
	
@app.route('/about')
def about():
	return 'This is About Page.'

if __name__ == '__main__':
   app.run(debug=True)