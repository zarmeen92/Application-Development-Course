from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
   #return 'Hello World'
   return render_template('index.html')

@app.route('/second/')
def second():
    return render_template('second.html')

@app.route('/marks/')
def marks():
    return render_template('marks.html')

@app.route('/submitform/',method=['post'])
def submitform():
	result = request.form
	return render_template('result.html',result=result)

if __name__ == '__main__':
   app.run(debug=True)