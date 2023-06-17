# Cấu hình bot và mã thông báo truy cập
# bot_token = '6103558882:AAG4VYtrGZbMWGCS9DhYMf1kmg3Vb_uF6Mo'
# bot_chatID = '-1001896695563'
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Cấu hình bot và mã thông báo truy cập
bot_token = '6103558882:AAG4VYtrGZbMWGCS9DhYMf1kmg3Vb_uF6Mo'
bot_chatID = '-1001896695563'

# Danh sách các tin nhắn đã gửi
sent_messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form.get('message')
        send_message(message)
        sent_messages.append(message)
    return render_template('index.html', sent_messages=sent_messages)

@app.route('/send_message', methods=['POST'])
def send_message_endpoint():
    message = request.form.get('message')
    send_message(message)
    sent_messages.append(message)
    return jsonify({'success': True})

def send_message(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': bot_chatID,
        'text': message
    }
    response = requests.post(url, params=params)

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': sent_messages})

if __name__ == '__main__':
    app.run()
