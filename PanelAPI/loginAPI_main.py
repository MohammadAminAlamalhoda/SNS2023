import flask
from flask import Flask, jsonify
import sys
sys.path.append('../Database')

import configs

app = Flask(__name__)

@app.route('/panel', methods=['GET', 'POST'])
def panel():
    if flask.request.method == "POST":
        data = flask.request.get_json()
        print(data)
        snsID = data['snsID']
        cursor = db.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE snsID = ?', (snsID,))
        user_info = cursor.fetchall()
        return flask.render_template('panel.html', user_info=user_info)
    else:
        return jsonify({'Error':'500'})



if __name__ == '__main__':
    db = configs.database_configs()
    app.run(host='0.0.0.0', port=105)