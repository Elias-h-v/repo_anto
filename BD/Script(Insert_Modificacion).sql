insert into perfiles (id_perfil, nombre_perfil)
values 
(1,'Administrador'),
(2,'Socio');

insert into tipo_certificados (id_tipo_certificado, nombre_tipo_certificado)
values
(1,'Certificado de Residencia'),
(2,'Certificado de Comisión'),
(3,'Certificado de Grupo Familiar'),
(4,'Certificado de Socio');

-- Eliminar la restricción FK
ALTER TABLE socios
DROP FOREIGN KEY socios_ibfk_3;
-- Editar tabla parentescos para cargar datos 
ALTER TABLE parentescos
MODIFY COLUMN id_parentesco INT AUTO_INCREMENT;

INSERT INTO parentescos (nombre_parentesco) VALUES
('Padre'),
('Madre'),
('Hijo'),
('Hija'),
('Abuelo'),
('Abuela'),
('Nieto'),
('Nieta'),
('Hermano'),
('Hermana'),
('Tío'),
('Tía'),
('Primo'),
('Prima'),
('Esposo'),
('Esposa'),
('Suegro'),
('Suegra'),
('Yerno'),
('Nuera');

-- Recrear la restricción de clave foránea con un nombre anterior
ALTER TABLE socios
ADD CONSTRAINT socios_ibfk_3 FOREIGN KEY (id_parentesco) REFERENCES parentescos (id_parentesco);

-- Eliminar restriccion de tabla comisiones 
ALTER TABLE comisiones
DROP FOREIGN KEY comisiones_ibfk_1;
-- Editar tabla tipo_comisiones para cargar datos 
ALTER TABLE tipo_comisiones 
MODIFY COLUMN id_tipo_comision INT AUTO_INCREMENT;

insert into tipo_comisiones (nombre_comision)
values
('Tesorería'),
('Actividades Sociales'),
('Emprendimientos'),
('Proyectos');
-- Recrear la restricción de clave foránea con un nombre anterior
ALTER TABLE comisiones 
ADD CONSTRAINT comisiones_ibfk_1 FOREIGN KEY (id_tipo_comision) REFERENCES tipo_comisiones (id_tipo_comision);

-- Eliminar columna erronea
ALTER TABLE socios
DROP COLUMN ide_comision;

-- Insertar más datos actualizados
INSERT INTO socios (rut, nombre, apellido, direccion, fecha_nacimiento, telefono, correo, estado_civil, jefe_hogar, id_parentesco, id_perfil)
VALUES 
('55556666-7', 'Marina', 'Perez', 'Avenida M #202', '1979-03-30', 777666555, 'marina.perez@example.com', 'casado', TRUE, 1, 2),
('77778888-9', 'Laura', 'Gutierrez', 'Avenida O #404', '1986-05-22', 999888777, 'laura.gutierrez@example.com', 'casado', TRUE, 3, 2),
('88889999-0', 'Diego', 'Rodriguez', 'Calle P #505', '1981-12-10', 111000999, 'diego.rodriguez@example.com', 'soltero', FALSE, 4, 1),
('99990000-1', 'Carmen', 'Lopez', 'Avenida Q #606', '1990-08-15', 222111000, 'carmen.lopez@example.com', 'casado', TRUE, 5, 2),
('10111213-4', 'Gabriel', 'Hernandez', 'Calle R #707', '1985-02-28', 333222111, 'gabriel.hernandez@example.com', 'soltero', FALSE, 6, 2),
('13141516-5', 'Valentina', 'Diaz', 'Avenida S #808', '1993-09-05', 444333222, 'valentina.diaz@example.com', 'casado', TRUE, 7, 2),
('18192021-2', 'Javier', 'Martinez', 'Calle T #909', '1980-04-18', 555444333, 'javier.martinez@example.com', 'soltero', FALSE, 8, 2),
('21222324-3', 'Camila', 'Gomez', 'Avenida U #1010', '1998-12-01', 666555444, 'camila.gomez@example.com', 'casado', TRUE, 9, 2),
('56456456-9', 'Lorena', 'Gonzalez', 'Calle V #111', '1989-08-12', 555444333, 'lorena.gonzalez@example.com', 'soltero', FALSE, 10, 2),
('45678901-2', 'Julio', 'Martinez', 'Avenida W #222', '1977-03-25', 666555444, 'julio.martinez@example.com', 'casado', TRUE, 11, 2),
('56789012-3', 'Carolina', 'Fernandez', 'Calle X #333', '1994-01-05', 777666555, 'carolina.fernandez@example.com', 'soltero', FALSE, 12, 2),
('67890123-4', 'Raul', 'Lopez', 'Avenida Y #444', '1982-11-18', 888777666, 'raul.lopez@example.com', 'casado', TRUE, 13, 2),
('78901234-5', 'Silvia', 'Ramirez', 'Calle Z #555', '1996-06-30', 999888777, 'silvia.ramirez@example.com', 'soltero', FALSE, 14, 2),
('89012345-6', 'Pedro', 'Gutierrez', 'Avenida AA #666', '1984-09-22', 111000999, 'pedro.gutierrez@example.com', 'casado', TRUE, 15, 2),
('90123456-7', 'Eva', 'Hernandez', 'Calle BB #777', '1990-04-15', 222111000, 'eva.hernandez@example.com', 'soltero', FALSE, 16, 2),
('01234567-8', 'Gustavo', 'Diaz', 'Avenida CC #888', '1987-12-02', 333222111, 'gustavo.diaz@example.com', 'casado', TRUE, 17, 2),
('12345678-9', 'Natalia', 'Sanchez', 'Calle DD #999', '1998-05-20', 444333222, 'natalia.sanchez@example.com', 'soltero', FALSE, 18, 2),
('23456789-0', 'Hector', 'Perez', 'Avenida EE #1010', '1979-02-10', 555444333, 'hector.perez@example.com', 'casado', TRUE, 19, 2),
('34567890-1', 'Ana', 'Martinez', 'Calle FF #1111', '1985-07-15', 666555444, 'ana.martinez@example.com', 'soltero', FALSE, 20, 2),
('45456457-9', 'Manuel', 'Gomez', 'Avenida GG #1212', '1993-03-08', 777666555, 'manuel.gomez@example.com', 'casado', TRUE, 1, 2),
('56789012-0', 'Fernanda', 'Ramirez', 'Calle HH #1313', '1980-11-28', 888777666, 'fernanda.ramirez@example.com', 'soltero', FALSE, 2, 2),
('67890723-4', 'Mario', 'Lopez', 'Avenida II #1414', '1997-06-10', 999888777, 'mario.lopez@example.com', 'casado', TRUE, 3, 2),
('78901234-0', 'Luisa', 'Gutierrez', 'Calle JJ #1515', '1983-09-18', 111000999, 'luisa.gutierrez@example.com', 'soltero', FALSE, 4, 2),
('89012345-0', 'Roberto', 'Fernandez', 'Avenida KK #1616', '1991-04-05', 222111000, 'roberto.fernandez@example.com', 'casado', TRUE, 5, 2);

