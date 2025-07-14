CREATE INDEX id_customers ON orders (customer_id);

CREATE INDEX id_price ON order_items (order_id, price);

CREATE INDEX idx_products ON order_items(product_name);

EXPLAIN ANALYZE SELECT order_id, price
                 FROM order_items
				 WHERE price > 1000 AND order_id = 123;


EXPLAIN ANALYZE SELECT customer_id
                FROM orders
			    WHERE customer_id = 1;



DROP INDEX IF EXISTS id_customers 

COMMENT ON TABLE orders IS 'Индекс был удален, так как он не использовался.';

