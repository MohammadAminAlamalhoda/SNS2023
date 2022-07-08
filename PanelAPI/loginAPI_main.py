from flask import Flask

app = Flask(__name__)
@app.route('/Panel', methods=['GET', 'POST'])
def welcome():
    return jsonify({'name':'Alam',
                    'address':'In front of the computer'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)