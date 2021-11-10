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

@app.route('/submitform/',methods=['post'])
def submitform():
	result = request.form
	return render_template('result2.html',result=result)
@app.route('/fileupload/')
def upload():  
    return render_template("fileupload.html")  
 
@app.route('/savefile', methods = ['POST'])  
def savefile():  
    f = request.files['userfile']  
    f.save(f.filename)  
    return render_template("success.html", name = f.filename)  
if __name__ == '__main__':
   app.run(debug=True)