from flask import Flask
app = Flask(__name__)

@app.route('/api/getusers')
def hello():
    return '[ {"user": "geert", "group": "admins"}, {"user": "bobby", "group": "users"} ]'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
