from flask import jsonify, current_app as app, render_template, send_file
from .models import db, User, ReceivedMessage, SentMessage, Catalogue
from .utils import generate_catalogue_pdf


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


@app.route('/messages/<int:user_id>', methods=['GET'])
def get_user_messages(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    received_messages = ReceivedMessage.query.filter_by(user_id=user_id).all()
    sent_messages = SentMessage.query.filter_by(user_id=user_id).all()

    received_list = []
    for message in received_messages:
        received_list.append({
            'id': message.id,
            'time_stamp': message.time_stamp,
            'text_content': message.text_content,
            'media_url': message.media_url,
            'is_read': message.is_read,
            'media_type_id': message.media_type_id,
            'message_type_id': message.message_type_id
        })

    sent_list = []
    for message in sent_messages:
        sent_list.append({
            'id': message.id,
            'time_stamp': message.time_stamp,
            'text_content': message.text_content,
            'media_url': message.media_url,
            'is_read': message.is_read,
            'media_type_id': message.media_type_id,
            'message_type_id': message.message_type_id
        })

    return jsonify({
        'user': {
            'id': user.id,
            'name': user.name,
            'phone_number': user.phone_number,
            'email': user.email
        },
        'received_messages': received_list,
        'sent_messages': sent_list
    })


@app.route('/catalogue/in_stock', methods=['GET'])
def get_in_stock_catalogue():
    in_stock_products = Catalogue.query.filter_by(True).all()

    products_list = []
    for product in in_stock_products:
        products_list.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'sell_price': product.sell_price,
            'catalogue_type_id': product.catalogue_type_id,
        })

    return jsonify({'in_stock_products': products_list})

@app.route('/catalogue/in_stock/pdf', methods=['GET'])
def get_in_stock_catalogue_pdf():
    in_stock_products = Catalogue.query.filter(Catalogue.cost_price > 0).all()

    filename = '..\in_stock_catalogue.pdf'
    generate_catalogue_pdf(in_stock_products, filename)

    return send_file(filename, as_attachment=True)