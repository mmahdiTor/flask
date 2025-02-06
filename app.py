from flask import Flask

app = Flask(__name__)

@app.route('/users')
def home():
    return "سلام! اپ Flask روی Render اجرا شد! 🚀"

if __name__ == '__main__':
    app.run(debug=True)
