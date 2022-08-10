from cgitb import text
from flask import Flask, request, render_template, redirect

nextId = 4

topics = {{'id':1, 'title': 'cat', 'body': 'cat on the skateboard'}, 
        {'id':2, 'title': 'dog', 'body': 'dog on the roof'}, 
        {'id':3, 'title': 'wolf', 'body': 'wolf on the mountain'}}


app = Flask(__name__)

# html template
def template(contents, content, id=None):
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
            <li><form action="/delete/{id}/" method="POST"><input type="submit" value="delete"></form></li>
        '''
    
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
                {contextUI}
            </ul>
        </body>
    </html>
    '''

# html linked in contents
def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

# main
@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')

# read
@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f"<h2>{title}</h2>{body}", id)

# create
@app.route('/create/', methods=['GET', 'POST'])
def create():
    print('request.method', request.method)
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="tilte"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title'] # title 입력 값을 받아옴
        body = request.form['body']
        newTopic = {'id': nextId, 'title': title, 'body' : body} # Topic 에 저장할 새로운 토픽을 생성
        topics.append(newTopic)
        url = '/read/' + str(nextId) +'/'
        nextId += 1
        return redirect(url) # 경로로 이동할 수 있도록 함
    


# update
@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    #print('request.method', request.method)
    if request.method == 'GET':
        title = ''
        body = ''
        for topic in topics:
            if id == topic['id']:
                title = topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" name="title" placeholder="tilte" value={title}></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="update"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title'] # title 입력 값을 받아옴
        body = request.form['body']
        for topic in topics:
            if id == topic['id']:
                topic['title'] = title
                topic['body'] = body
                break

        url = '/read/' + str(id) +'/'
        return redirect(url) # 경로로 이동할 수 있도록 함
    
# delete 
@app.route('/delete/<int:id>/', methods=['POST'])
def delete(id):
    for topic in topics:
        if id == topic['id']:
            topics.remove(topic)
            break
    return redirect('/')
    

app.run(debug=True)
#app.run(port=5001, debug=True)
# 실제 서비스 시에는 debug mode is not useful