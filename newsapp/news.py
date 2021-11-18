from flask import *
import requests

app = Flask(__name__)


@app.route('/')
def index():
	url = 'https://api.thenewsapi.com/v1/news/top?api_token=U4kBMfgXdiPDGs4VLmlVZ8ZhPlZ4z9u0vYrAB5yo&locale=us&limit=5'
	response = requests.get(url).json()
	print(response['data'])
	return render_template('index.html',news=response['data'])
@app.route('/searchnews',methods=['POST'])
def searchnews():
	query=request.form
	print(query['searchnews'])
	url = 'https://api.thenewsapi.com/v1/news/all?api_token=U4kBMfgXdiPDGs4VLmlVZ8ZhPlZ4z9u0vYrAB5yo&search='+query['searchnews']
	response = requests.get(url).json()
	print(response['data'])
	return render_template('index.html',news=response['data'])

if __name__ == '__main__':
    app.run(debug=True)