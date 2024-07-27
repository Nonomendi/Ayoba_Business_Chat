from app import create_app, db
from app.models import User, MessageType, MediaType, ReceivedMessage, SentMessage, CatalogueType, Catalogue, Sale

def initialize_database():
    app = create_app()
    with app.app_context():
        db.create_all()
    
        # Insert mock data
        user1 = User(phone_number='1234567890', name='Alice Johnson', email='alice@example.com')
        user2 = User(phone_number='2345678901', name='Bob Smith', email='bob@example.com')
        user3 = User(phone_number='3456789012', name='Carol Williams', email='carol@example.com')
        
        message_type1 = MessageType(name='text')
        message_type2 = MessageType(name='media')
        
        media_type1 = MediaType(name='Image')
        media_type2 = MediaType(name='Audio')
        media_type3 = MediaType(name='Video')
        
        received_message1 = ReceivedMessage(time_stamp='2024-07-25 10:00:00', text_content='Hello Alice!', is_read=1, message_type_id=1, user_id=1)
        received_message2 = ReceivedMessage(time_stamp='2024-07-25 10:05:00', media_url='http://example.com/image.jpg', is_read=0, media_type_id=1, message_type_id=2, user_id=1)
        received_message3 = ReceivedMessage(time_stamp='2024-07-25 10:10:00', text_content='Hi Bob!', is_read=1, message_type_id=1, user_id=2)
        received_message4 = ReceivedMessage(time_stamp='2024-07-25 10:15:00', media_url='http://example.com/audio.mp3', is_read=0, media_type_id=2, message_type_id=2, user_id=2)
        received_message5 = ReceivedMessage(time_stamp='2024-07-25 10:20:00', text_content='Hello Carol!', is_read=1, message_type_id=1, user_id=3)
        
        sent_message1 = SentMessage(time_stamp='2024-07-25 11:00:00', text_content='Hi Alice, how are you?', is_read=1, message_type_id=1, user_id=1)
        sent_message2 = SentMessage(time_stamp='2024-07-25 11:05:00', media_url='http://example.com/video.mp4', is_read=0, media_type_id=3, message_type_id=2, user_id=1)
        sent_message3 = SentMessage(time_stamp='2024-07-25 11:10:00', text_content='Hi Bob, please check this.', is_read=1, message_type_id=1, user_id=2)
        sent_message4 = SentMessage(time_stamp='2024-07-25 11:15:00', media_url='http://example.com/image2.jpg', is_read=0, media_type_id=1, message_type_id=2, user_id=2)
        sent_message5 = SentMessage(time_stamp='2024-07-25 11:20:00', text_content='Hi Carol, here is the document.', is_read=1, message_type_id=1, user_id=3)
        
        catalogue_type1 = CatalogueType(name='products')
        catalogue_type2 = CatalogueType(name='services')
        
        catalogue1 = Catalogue(name='Laptop', description='High performance laptop',cost_price=599.99, sell_price=999.99, catalogue_type_id=1)
        catalogue2 = Catalogue(name='Smartphone', description='Latest model smartphone',cost_price=499.99, sell_price=799.99, catalogue_type_id=1)
        catalogue3 = Catalogue(name='Web Development', description='Web Development service, priced per hour', cost_price=0, sell_price=299.99, catalogue_type_id=2)
        catalogue4 = Catalogue(name='Gardening', description='Gardening service, price per square meter', cost_price=5.00, sell_price=14.99, catalogue_type_id=2)
        
        sale1 = Sale(quantity=1, user_id=1, catalogue_id=1)
        sale2 = Sale(quantity=2, user_id=2, catalogue_id=3)
        sale3 = Sale(quantity=3, user_id=3, catalogue_id=4)
        
        db.session.add_all([user1, user2, user3, message_type1, message_type2, media_type1, media_type2, media_type3,
                            received_message1, received_message2, received_message3, received_message4, received_message5,
                            sent_message1, sent_message2, sent_message3, sent_message4, sent_message5,
                            catalogue_type1, catalogue_type2, catalogue1, catalogue2, catalogue3, catalogue4,
                            sale1, sale2, sale3])
        
        db.session.commit()

if __name__ == '__main__':
    initialize_database()

