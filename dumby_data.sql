INSERT INTO `users` (`phone_number`, `name`, `email`) VALUES
('1234567890', 'Alice Johnson', 'alice@example.com'),
('2345678901', 'Bob Smith', 'bob@example.com'),
('3456789012', 'Carol Williams', 'carol@example.com');

INSERT INTO `message_types` (`name`) VALUES
('text'),
('media');

INSERT INTO `media_types` (`name`) VALUES
('image'),
('audio'),
('video');

-- Insert mock data into the `received_messages` table
INSERT INTO `received_messages` (`time_stamp`, `text_content`, `media_url`, `is_read`, `media_type_id`, `message_type_id`, `user_id`) VALUES
('2024-07-25 10:00:00', 'Hello Alice!', NULL, 1, NULL, 1, 1),
('2024-07-25 10:05:00', NULL, 'http://example.com/image.jpg', 0, 1, 2, 1),
('2024-07-25 10:10:00', 'Hi Bob!', NULL, 1, NULL, 1, 2),
('2024-07-25 10:15:00', NULL, 'http://example.com/audio.mp3', 0, 2, 2, 2),
('2024-07-25 10:20:00', 'Hello Carol!', NULL, 1, NULL, 1, 3);

-- Insert mock data into the `sent_messages` table
INSERT INTO `sent_messages` (`time_stamp`, `text_content`, `media_url`, `is_read`, `media_type_id`, `message_type_id`, `user_id`) VALUES
('2024-07-25 11:00:00', 'Hi Alice, how are you?', NULL, 1, NULL, 1, 1),
('2024-07-25 11:05:00', NULL, 'http://example.com/video.mp4', 0, 3, 2, 1),
('2024-07-25 11:10:00', 'Hi Bob, please check this.', NULL, 1, NULL, 1, 2),
('2024-07-25 11:15:00', NULL, 'http://example.com/image2.jpg', 0, 1, 2, 2),
('2024-07-25 11:20:00', 'Hi Carol, here is the document.', NULL, 1, NULL, 1, 3);

-- Insert mock data into the `catalogue_types` table
INSERT INTO `catalogue_types` (`name`) VALUES
('product'),
('service');

-- Insert mock data into the `catalogue` table
INSERT INTO `catalogue` (`name`, `description`, `cost_price`, `sell_price`, `catalogue_type_id`) VALUES
('Laptop', 'High performance laptop', 499.99, 999.99, 1),
('Smartphone', 'Latest model smartphone', 399.99, 799.99, 1),
('IT Web Design', 'Website design, price is per hour rate', 0, 199.99, 2),
('Gardening', 'Gardening service, price is per square meter', 2.00, 14.99, 2);

-- Insert mock data into the `Sales` table
INSERT INTO `Sales` (`quantity`, `user_id`, `catalogue_id`) VALUES
(1, 1, 1),
(2, 2, 3),
(3, 3, 4);
