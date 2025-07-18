
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,        
    name VARCHAR(100) NOT NULL,    
    email VARCHAR(200) UNIQUE       
);


CREATE TABLE orders (
    id SERIAL PRIMARY KEY,        
    customer_id INT,                
    order_date DATE NOT NULL,      
    FOREIGN KEY (customer_id) REFERENCES customers(id) 
);


CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,         
    order_id INT,                  
    product_name VARCHAR(300) NOT NULL,  
    quantity INT NOT NULL,         
    price NUMERIC(10, 2) NOT NULL,  
    FOREIGN KEY (order_id) REFERENCES orders(id)  
);

INSERT INTO customers (name , email) VALUES
('Иван Иванов', 'ivan@example.com'),
('Мария Петрова', 'maria@example.com'),
('Алексей Смирнов', 'alexey@example.com');


INSERT INTO orders (customer_id, order_date) VALUES
(1, '07.06.2025'),
(1, '05.03.2024'),
(2, '07.04.2025'),
(3, '03.01.2025'),
(1, '21.05.2025');

INSERT INTO order_items (order_id, product_name, quantity, price) VALUES
(1, 'Товар 1', 3, 19.99),
(2, 'Товар-2', 5, 1000),
(3, 'Товар-3', 13, 15000),
(3, 'Товар-4', 1, 199.98),
(5, 'Товар-5', 199, 24.67 )


SELECT o.id, o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE c.name = 'Иван Иванов';

SELECT s.product_name, s.quantity, s.price
FROM order_items s
JOIN orders o ON s.order_id = o.id
WHERE o.id = 3
ORDER BY s.price DESC

SELECT c.name, SUM(oi.price * oi.quantity)
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
GROUP BY c.name
HAVING SUM(oi.price * oi.quantity)> 5000;

