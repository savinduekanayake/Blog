from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name,id):
    return "hello, " + name + " your id is: " + str(id)


@app.route('/onlyget', methods=['GET'])
def get_req():
    return "you can only get this webpage"

if __name__ == "__main__":
    app.run(debug=True)



