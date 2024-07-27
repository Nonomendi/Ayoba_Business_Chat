from flask import jsonify, current_app as app, render_template
from .models import db, User, ReceivedMessage, SentMessage


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/users_with_messages', methods=['GET'])
def get_users_with_messages():
    users_with_received_messages = db.session.query(User).join(ReceivedMessage, User.id == ReceivedMessage.user_id).all()
    users_with_sent_messages = db.session.query(User).join(SentMessage, User.id == SentMessage.user_id).all()
    
    # Combine the lists and remove duplicates
    all_users = list(set(users_with_received_messages + users_with_sent_messages))
    
    users_list = []
    for user in all_users:
        users_list.append({
            'id': user.id,
            'name': user.name,
            'phone_number': user.phone_number,
            'email': user.email
        })

    return jsonify({'users': users_list})