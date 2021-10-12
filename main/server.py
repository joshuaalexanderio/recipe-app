from flask import Flask, render_template, request

app = Flask(__name__)

#  Default index route
@app.route('/')
def index():
  return render_template('index.html')

# Run python code at given directory 
@app.route('/send-eng-muff', methods=['GET', 'POST'])
def send_eng_muff():
  print ('I got clicked!')
  import requests, uuid, json
  from bs4 import BeautifulSoup
  from urllib.request import urlopen
  with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
  if request.method == 'POST': 
    className = request.form['eng-muff']
    html_tags = soup.find_all('li', attrs={'class': className})
    for el in html_tags:
      print (el.get_text())
      requests.post(
      "https://api.todoist.com/rest/v1/tasks",
      data=json.dumps({
          "content": el.text,
          "project_id": 2275814810
      }),
      headers={
          "Content-Type": "application/json",
          "X-Request-Id": str(uuid.uuid4()),
          "Authorization": "Bearer 0123456789abcdef0123456789"
      }).json()
  return render_template('index.html')
@app.route('/send-chicken-salad', methods=['GET', 'POST'])
def send_chicken_salad():
  print ('I got clicked!')
  import requests, uuid, json
  from bs4 import BeautifulSoup
  from urllib.request import urlopen
  with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
  if request.method == 'POST': 
    className = request.form['chicken-salad']
    html_tags = soup.find_all('li', attrs={'class': className})
    for el in html_tags:
      print (el.get_text())
      requests.post(
      "https://api.todoist.com/rest/v1/tasks",
      data=json.dumps({
          "content": el.text,
          "project_id": 2275814810
      }),
      headers={
          "Content-Type": "application/json",
          "X-Request-Id": str(uuid.uuid4()),
          "Authorization": "Bearer 0123456789abcdef0123456789"
      }).json()
  return render_template('index.html')

@app.route('/send-orzo-salad', methods=['GET', 'POST'])
def send_orzo_salad():
  print ('I got clicked!')
  import requests, uuid, json
  from bs4 import BeautifulSoup
  from urllib.request import urlopen
  with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
  if request.method == 'POST': 
    className = request.form['orzo-salad']
    html_tags = soup.find_all('li', attrs={'class': className})
    for el in html_tags:
      print (el.get_text())
      requests.post(
      "https://api.todoist.com/rest/v1/tasks",
      data=json.dumps({
          "content": el.text,
          "project_id": 2275814810
      }),
      headers={
          "Content-Type": "application/json",
          "X-Request-Id": str(uuid.uuid4()),
          "Authorization": "Bearer 0123456789abcdef0123456789"
      }).json()
  return render_template('index.html')

@app.route('/send-chicken-burrito', methods=['GET', 'POST'])
def send_chicken_burrito  ():
  print ('I got clicked!')
  import requests, uuid, json
  from bs4 import BeautifulSoup
  from urllib.request import urlopen
  with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
  if request.method == 'POST': 
    className = request.form['chicken-burrito']
    html_tags = soup.find_all('li', attrs={'class': className})
    for el in html_tags:
      print (el.get_text())
      requests.post(
      "https://api.todoist.com/rest/v1/tasks",
      data=json.dumps({
          "content": el.text,
          "project_id": 2275814810
      }),
      headers={
          "Content-Type": "application/json",
          "X-Request-Id": str(uuid.uuid4()),
          "Authorization": "Bearer 0123456789abcdef0123456789"
      }).json()
  return render_template('index.html')

@app.route('/send-cart-chicken', methods=['GET', 'POST'])
def send_cart_chicken():
  print ('I got clicked!')
  import requests, uuid, json
  from bs4 import BeautifulSoup
  from urllib.request import urlopen
  with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
  if request.method == 'POST': 
    className = request.form['cart-chicken']
    html_tags = soup.find_all('li', attrs={'class': className})
    for el in html_tags:
      print (el.get_text())
      requests.post(
      "https://api.todoist.com/rest/v1/tasks",
      data=json.dumps({
          "content": el.text,
          "project_id": 2275814810
      }),
      headers={
          "Content-Type": "application/json",
          "X-Request-Id": str(uuid.uuid4()),
          "Authorization": "Bearer 0123456789abcdef0123456789"
      }).json()
  return render_template('index.html')

@app.route('/send-ricotta-pasta', methods=['GET', 'POST'])
def send_ricotta_pasta():
  print ('I got clicked!')
  import requests, uuid, json
  from bs4 import BeautifulSoup
  from urllib.request import urlopen
  with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
  if request.method == 'POST': 
    className = request.form['ricotta-pasta']
    html_tags = soup.find_all('li', attrs={'class': className})
    for el in html_tags:
      print (el.get_text())
      requests.post(
      "https://api.todoist.com/rest/v1/tasks",
      data=json.dumps({
          "content": el.text,
          "project_id": 2275814810
      }),
      headers={
          "Content-Type": "application/json",
          "X-Request-Id": str(uuid.uuid4()),
          "Authorization": "Bearer 0123456789abcdef0123456789"
      }).json()
  return render_template('index.html')
  
if __name__ == '__main__':
  app.run(debug=True)