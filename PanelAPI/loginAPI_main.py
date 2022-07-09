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
        snsID = data['snsID']
        name = data['name']
        email = data['email']
        lunchs = 2
        snacks = 2
        cursor = db.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE snsID = ?', (snsID,))
        user_info = cursor.fetchall()
        if len(user_info)==0:
            cursor.execute('INSERT INTO users (snsID, name, email, lunchs, snacks) VALUES (?, ?, ?, ?, ?)',
                             (snsID, name, email, lunchs, snacks))
            db.conn.commit()
        cursor.execute('SELECT * FROM users WHERE snsID = ?', (snsID,))
        user_info = cursor.fetchall()
        print(user_info)
        return flask.render_template('panel.html', user_info=user_info[0])
    else:
        return jsonify({'status':'500 Error'})



if __name__ == '__main__':
    db = configs.database_configs()
    app.run(host='0.0.0.0', port=105)