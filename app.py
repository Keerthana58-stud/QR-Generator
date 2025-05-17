from flask import Flask, request, render_template
import qrcode
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'static/qr_codes'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    qr_image_url = None

    if request.method == 'POST':
        data = request.form['qrtext']
        filename = f"qr_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        path = os.path.join(UPLOAD_FOLDER, filename)

        img = qrcode.make(data)
        img.save(path)

        qr_image_url = f"/static/qr_codes/{filename}"

    return render_template('index.html', qr_image_url=qr_image_url)

if __name__ == '__main__':
    app.run(debug=True)
