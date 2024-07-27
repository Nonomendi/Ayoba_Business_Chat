CREATE TABLE `users` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `phone_number` TEXT,
  `name` TEXT,
  `email` TEXT
);

CREATE TABLE `message_types` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT
);

CREATE TABLE `media_types` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT
);

CREATE TABLE `received_messages` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `time_stamp` TEXT,
  `text_content` TEXT,
  `media_url` TEXT,
  `is_read` INTEGER,
  `media_type_id` INTEGER,
  `message_type_id` INTEGER,
  `user_id` INTEGER,
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
  FOREIGN KEY (`media_type_id`) REFERENCES `media_types`(`id`),
  FOREIGN KEY (`message_type_id`) REFERENCES `message_types`(`id`)
);

CREATE TABLE `sent_messages` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `time_stamp` TEXT,
  `text_content` TEXT,
  `media_url` TEXT,
  `is_read` INTEGER,
  `media_type_id` INTEGER,
  `message_type_id` INTEGER,
  `user_id` INTEGER,
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
  FOREIGN KEY (`media_type_id`) REFERENCES `media_types`(`id`),
  FOREIGN KEY (`message_type_id`) REFERENCES `message_types`(`id`)
);

CREATE TABLE `catalogue_types` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT
);

CREATE TABLE `catalogue` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT,
  `description` TEXT,
  `cost_price` REAL,
  `sell_price` REAL,
  `catalogue_type_id` INTEGER,
  FOREIGN KEY (`catalogue_type_id`) REFERENCES `catalogue_types`(`id`)
);

CREATE TABLE `Sales` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `quantity` INTEGER,
  `user_id` INTEGER,
  `catalogue_id` INTEGER,
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
  FOREIGN KEY (`catalogue_id`) REFERENCES `catalogue`(`id`)
);




