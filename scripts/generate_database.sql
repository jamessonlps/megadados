DROP DATABASE IF EXISTS inventario;
CREATE DATABASE inventario;

USE inventario;
CREATE TABLE IF NOT EXISTS products (
	id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(32) NOT NULL,
    brand VARCHAR(32) NOT NULL,
    description VARCHAR(256),
    price FLOAT NOT NULL,
    PRIMARY KEY (id),
    CHECK (price >= 0)
);

CREATE TABLE IF NOT EXISTS inventory (
	id INT NOT NULL AUTO_INCREMENT,
    product_id INT NOT NULL UNIQUE,
    amount INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (product_id)
		REFERENCES products(id)
        ON DELETE CASCADE,
	CHECK (amount >= 0)
);

CREATE TABLE IF NOT EXISTS transactions (
	id INT NOT NULL AUTO_INCREMENT,
    quantity INT NOT NULL,
    product_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (product_id)
		REFERENCES products(id)
        ON DELETE CASCADE
);

INSERT INTO products (name, brand, description, price) VALUES
	("guarana jesus", "Coca", "Bebida do Maranhao!!!", 10),
    ("coquinha zero", "Coca", "Melhor refri de todos os tempos", 5.5),
    ("queijo dos deuses", "Qualita", "Com cuscuz e ovo fica top!", 8.5),
    ("pao celestial", "Santa Padaria", "Só perde pro cuscuz com ovo", 2.2);
    
INSERT INTO inventory (product_id, amount) VALUES
	(1, 10),
    (2, 2),
    (3, 5),
    (4, 0);