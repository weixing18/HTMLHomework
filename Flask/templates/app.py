from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 处理用户登录逻辑
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'POST':
        # 处理用户留言逻辑
        return redirect(url_for('messages'))
    return render_template('messages.html')

if __name__ == '__main__':
    app.run()
