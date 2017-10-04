from django.db import models


class User(models.Model):
    user_identify_number = models.UUIDField(default=0, primary_key=True, editable=True)  # Clave primaria
    user_name = models.CharField(max_length=200)
    user_lastName = models.CharField(max_length=200)
    user_born_date = models.DateTimeField('BirthDay Date')
    user_id_identify_Type = models.IntegerField(default=0)   # id del tipo de identificacion
    # user_id_country = models.IntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)  # id del pais de origen
    user_email = models.EmailField(null=False)

    class Meta:
        db_table = 'user'


class Country(models.Model):
    numeric_code = models.UUIDField(primary_key=True, editable=False) #models.CharField(max_length=3)
    alpha_2_code = models.CharField(max_length=2)
    alpha_3_code = models.CharField(max_length=3)
    eng = models.CharField(max_length=44)
    spa = models.CharField(max_length=44)

    class Meta:
        db_table = 'iso_3166_1'


class StudyType(models.Model):
    study_type_id = models.UUIDField(primary_key=True, editable=True)
    eng = models.CharField(max_length=200)
    spa = models.CharField(max_length=200)

    class Meta:
        db_table = 'grado_estudio'


class Degree(models.Model):
    degree_id = models.UUIDField(primary_key=True, editable=True)
    eng = models.CharField(max_length=200)
    eng = models.CharField(max_length=200)

    class Meta:
        db_table = 'Licenciatura'


class StudyHistory(models.Model):
    institution = models.CharField(max_length=200)
    date_from = models.DateTimeField('Fecha de inicio')
    date_to = models.DateTimeField('Fecha fin')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.ForeignKey(StudyType, on_delete=models.CASCADE)
    studyType = models.ForeignKey(StudyType, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Historial_estudio'


class LaboralExp(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    position_functions = models.CharField(max_length=200)
    laboring_since = models.DateTimeField('Fecha de inicio')
    laboring_to = models.DateTimeField('Fecha fin')
    at_date = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'experiencia_laboral'


class PhoneCountryCode(models.Model):
    id = models.AutoField(max_length=11, primary_key=True)
    iso = models.CharField(max_length=2, null=False)
    name = models.CharField(max_length=80, null=False)
    nicename = models.CharField(max_length=80, null=False)
    iso3 = models.CharField(max_length=3, null=False)
    numcode = models.SmallIntegerField(max_length=6, null=False)
    phonecode = models.IntegerField(max_length=5, null=False)

    class Meta:
        db_table = 'telefono_cod_pais'


class PhoneType(models.Model):
    id = models.AutoField(max_length=11, primary_key=True)
    eng = models.CharField(max_length=100)
    eng = models.CharField(max_length=100)

    class Meta:
        db_table = 'telefono_tipo'


class PhoneNumber(models.Model):
    number = models.IntegerField(max_length=10, null=True)
    phoneCountryCode = models.ForeignKey(PhoneCountryCode, on_delete=models.CASCADE)
    phoneType = models.ForeignKey(PhoneType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'telefono_numero'


class Habilities(models.Model):
    skill_description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'habilidades'


class Aptitudes(models.Model):
    atitude_description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'aptitudes'