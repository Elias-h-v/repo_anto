# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Certificados(models.Model):
    id_certificado = models.AutoField(primary_key=True)
    id_tipo_certificado = models.ForeignKey('TipoCertificados', models.DO_NOTHING, db_column='id_tipo_certificado', blank=True, null=True)
    fecha_emision = models.DateField(blank=True, null=True)
    rut = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificados'


class Comisiones(models.Model):
    id_comision = models.AutoField(primary_key=True)
    rut = models.ForeignKey('Socios', models.DO_NOTHING, db_column='rut', blank=True, null=True)
    id_tipo_comision = models.ForeignKey('TipoComisiones', models.DO_NOTHING, db_column='id_tipo_comision', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comisiones'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GruposFamiliares(models.Model):
    id_grupo_familiar = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=255, blank=True, null=True)
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupos_familiares'
        unique_together = (('id_grupo_familiar', 'nombre', 'apellido', 'rut'),)


class Parentescos(models.Model):
    id_parentesco = models.IntegerField(primary_key=True)
    nombre_parentesco = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.nombre_parentesco
    class Meta:
        managed = False
        db_table = 'parentescos'


class Perfiles(models.Model):
    id_perfil = models.IntegerField(primary_key=True)
    nombre_perfil = models.CharField(max_length=13, blank=True, null=True)
    def __str__(self):
        return self.nombre_perfil
    class Meta:
        managed = False
        db_table = 'perfiles'


class Socios(models.Model):
    rut = models.CharField(primary_key=True, max_length=12, verbose_name='Rut')
    nombre = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nombres')
    apellido = models.CharField(max_length=255, blank=True, null=True, verbose_name='Apellidos')
    direccion = models.CharField(max_length=255, blank=True, null=True, verbose_name='Dirección')
    fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name='Fecha nacimiento')
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=255, blank=True, null=True)
    estado_civil = models.CharField(max_length=7, blank=True, null=True)
    jefe_hogar = models.IntegerField(blank=True, null=True)
    id_grupo_familiar = models.ForeignKey(GruposFamiliares, models.DO_NOTHING, db_column='id_grupo_familiar', blank=True, null=True)
    id_parentesco = models.ForeignKey(Parentescos, models.DO_NOTHING, db_column='id_parentesco', blank=True, null=True)
    id_certificado = models.IntegerField(blank=True, null=True)
    id_perfil = models.ForeignKey(Perfiles, models.DO_NOTHING, db_column='id_perfil', blank=True, null=True)
    def __str__(self):
        texto ="{0} {1} {2}"
        return texto.format(self.rut, self.nombre, self.apellido)
    class Meta:
        managed = False
        db_table = 'socios'


class TipoCertificados(models.Model):
    id_tipo_certificado = models.IntegerField(primary_key=True)
    nombre_tipo_certificado = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.nombre_tipo_certificado
    class Meta:
        managed = False
        db_table = 'tipo_certificados'


class TipoComisiones(models.Model):
    id_tipo_comision = models.IntegerField(primary_key=True)
    nombre_comision = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.nombre_comision
    class Meta:
        managed = False
        db_table = 'tipo_comisiones'


class UnionSocioCertificado(models.Model):
    id_certificado = models.ForeignKey(Certificados, models.DO_NOTHING, db_column='id_certificado', blank=True, null=True)
    rut = models.ForeignKey(Socios, models.DO_NOTHING, db_column='rut', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'union_socio_certificado'


class UnionSocioComision(models.Model):
    id_comision = models.ForeignKey(Comisiones, models.DO_NOTHING, db_column='id_comision', blank=True, null=True)
    rut = models.ForeignKey(Socios, models.DO_NOTHING, db_column='rut', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'union_socio_comision'
