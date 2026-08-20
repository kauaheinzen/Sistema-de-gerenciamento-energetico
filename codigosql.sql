CREATE DATABASE IF NOT EXISTS sistema_controle_energetico;
USE sistema_controle_energetico;

CREATE TABLE IF NOT EXISTS familia(
	id_familia INT AUTO_INCREMENT PRIMARY KEY,
	pessoas INT NOT NULL,
    consumo_total DECIMAL DEFAULT 0.00
);

CREATE TABLE IF NOT EXISTS eletrodomesticos(
	id_eletronico INT AUTO_INCREMENT PRIMARY KEY,
	nome_eletronico VARCHAR(100) NOT NULL,
	consumo FLOAT NOT NULL,
	horas_diarias FLOAT NOT NULL,
	fk_id_familia INT NOT NULL,
	
	FOREIGN KEY (fk_id_familia) REFERENCES familia(id_familia)
);

DELIMITER //

CREATE PROCEDURE atualizar_consumo_familia(IN id_familia INT)
BEGIN
    UPDATE familia 
    SET consumo_total = COALESCE(
        (SELECT SUM(consumo * horas_diarias * 30) 
         FROM eletrodomesticos 
         WHERE fk_id_familia = id_familia), 
        0.00
    )
    WHERE id_familia = id_familia;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER total_consumo_insert
AFTER INSERT ON eletrodomesticos
FOR EACH ROW
BEGIN
    CALL atualizar_consumo_familia(NEW.fk_id_familia);
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER total_consumo_update
AFTER UPDATE ON eletrodomesticos
FOR EACH ROW
BEGIN
    CALL atualizar_consumo_familia(NEW.fk_id_familia);
    IF OLD.fk_id_familia <> NEW.fk_id_familia THEN
        CALL atualizar_consumo_familia(OLD.fk_id_familia);
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER consumo_total_delete
AFTER DELETE ON eletrodomesticos
FOR EACH ROW
BEGIN
    CALL atualizar_consumo_familia(OLD.fk_id_familia);
END //

DELIMITER ;