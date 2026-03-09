from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    google_search_url = f'https://www.googleapis.com/customsearch/v1?key=YOUR_API_KEY&cx=YOUR_CX&q={{query}}'
    response = requests.get(google_search_url)
    results = response.json().get('items', [])
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
