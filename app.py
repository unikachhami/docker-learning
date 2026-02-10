from flask import Flask,render_template,request

app =Flask(__name__)
@app.route('/')
def index():
    return '''
        <html>
        <body>
        <form method="post" action="/greet">
            <input type="text" name="name" placeholder="Enter your name">
            <button type="submit">Greet me</button>
        </form>


'''

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', 'Stranger')
    return f"<h2>Hello, {name}! 🌱</h2>"

if __name__ == '__main__':
    app.run(debug=True)