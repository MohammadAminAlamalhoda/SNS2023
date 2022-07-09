import flask
from flask import Flask, jsonify
import sys
import io
from PIL import Image
sys.path.append('Database')
sys.path.append('QRCode')

import configs
import qrcode_configs


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
        user_info = cursor.fetchone()
        if len(user_info)==0:
            cursor.execute('INSERT INTO users (snsID, name, email, lunchs, snacks) VALUES (?, ?, ?, ?, ?)',
                             (snsID, name, email, lunchs, snacks))
            db.conn.commit()
            cursor.execute('SELECT * FROM users WHERE snsID = ?', (snsID,))
            user_info = cursor.fetchone()
        qr_image = qr.make_image(user_info)
        qr_image_arr = qr_image.tobytes().decode("latin1")
        html = flask.render_template('panel.html', user_info=user_info)
        return jsonify({'status':'success', 'html':html, 'qr_image':qr_image_arr})
    else:
        return jsonify({'status':'500 Error'})



if __name__ == '__main__':
    db = configs.database_configs()
    qr = qrcode_configs.QRCode()
    app.run(host='0.0.0.0', port=105)