CREATE TABLE perfiles (
id_perfil INT (1) PRIMARY KEY,
nombre_perfil VARCHAR(13)
);

CREATE TABLE parentescos (
id_parentesco INT (2) PRIMARY KEY,
nombre_parentesco VARCHAR (255)
);

CREATE TABLE socios (
rut VARCHAR(12) PRIMARY KEY,
nombre VARCHAR(255),
apellido VARCHAR(255),
direccion VARCHAR(255),
fecha_nacimiento DATE,
telefono INT(11) zerofill,
correo VARCHAR(255) DEFAULT 'No especifica',
estado_civil VARCHAR(7),
jefe_hogar BOOLEAN,
id_grupo_familiar INT (12),
id_parentesco INT (12),
id_certificado INT,
ide_comision INT (2),
id_perfil INT,
FOREIGN KEY (id_perfil) REFERENCES perfiles(id_perfil),
FOREIGN KEY (id_grupo_familiar) REFERENCES grupos_familiares(id_grupo_familiar),
FOREIGN KEY (id_parentesco) REFERENCES parentescos(id_parentesco)
);

CREATE TABLE grupos_familiares (
id_grupo_familiar INT AUTO_INCREMENT,
nombre_completo VARCHAR (255),
rut VARCHAR(12),
nombre VARCHAR(255),
apellido VARCHAR(255),
comentario VARCHAR (255),
CONSTRAINT pk_grupo_familiar PRIMARY KEY (id_grupo_familiar, nombre, apellido, rut)
);

CREATE TABLE certificados (
id_certificado INT AUTO_INCREMENT PRIMARY KEY,
id_tipo_certificado INT (2),
fecha_emision DATE,
rut INT (12),
FOREIGN KEY (id_tipo_certificado) REFERENCES tipo_certificados(id_tipo_certificado)
);

CREATE TABLE tipo_certificados (
id_tipo_certificado INT (2) PRIMARY KEY,
nombre_tipo_certificado VARCHAR (255)
);

CREATE TABLE union_socio_certificado (
id_certificado INT,
rut VARCHAR (12),
FOREIGN KEY (id_certificado) REFERENCES certificados(id_certificado),
FOREIGN KEY (rut) REFERENCES socios(rut)
);


CREATE TABLE comisiones (
id_comision INT (2) AUTO_INCREMENT PRIMARY KEY,
rut VARCHAR (12),
id_tipo_comision INT (2),
FOREIGN KEY (id_tipo_comision) REFERENCES tipo_comisiones(id_tipo_comision),
FOREIGN KEY (rut) REFERENCES socios(rut)
);

CREATE TABLE tipo_comisiones (
id_tipo_comision INT (2) PRIMARY KEY,
nombre_comision VARCHAR (255)
);

CREATE TABLE union_socio_comision (
id_comision INT,
rut VARCHAR (12),
FOREIGN KEY (id_comision) REFERENCES comisiones(id_comision),
FOREIGN KEY (rut) REFERENCES socios(rut)
);

SHOW CREATE DATABASE junta_vecinos;
