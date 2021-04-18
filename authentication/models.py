# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django_postgres_extensions.models.fields import ArrayField
class User(models.Model):
    mat_emp = models.CharField(default=None, max_length=20)
    cuid_emp = models.CharField(max_length=20, default=None)
    genre = models.CharField(max_length=20, default=None)
    nom_emp = models.CharField(
        'nom_emp',
        max_length=50,
        default=None

    )
    id_dept = models.CharField(max_length=20, default=None)
    nom_dept = models.CharField(max_length=100, default=None)
    matricul_resp = models.CharField(max_length=50, default=None)
    nom_resp = models.CharField(max_length=50, default=None)
    id_dept_parent = models.CharField(max_length=20, default=None)
    nom_dept_parent = models.CharField(max_length=50, default=None)
    name_bu = models.CharField(max_length=50, default=None)
    name_direction = models.CharField(max_length=50, default=None)
    resp_bu = models.CharField(max_length=50, default=None)
    mail = models.EmailField(unique=False, blank=False,
                             error_messages={
                                 'unique': "A user with that email already exists.",
                             },verbose_name='E_mail')
    nb_exp = models.CharField(max_length=20, default=None)
    seniorite = models.CharField(max_length=20, default=None)
    adresse_residence = models.CharField(max_length=30, blank=True, null=True)
    adresse_domicile = models.CharField(max_length=30, blank=True, null=True)
    Telephone_professionnel = models.CharField(max_length=30, blank=True, null=True)
    Telephone_personnel = models.CharField(max_length=30, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    post = ArrayField(models.CharField(max_length=24), blank=True, null=True, size=None)
    datede = ArrayField(models.CharField(max_length=24), blank=True, null=True, size=None)
    adate = ArrayField(models.CharField(max_length=24), blank=True, null=True, size=None)
    formation = models.CharField(max_length=100, null=True)
    certification = models.CharField(max_length=100, null=True)
    vie_associative = models.CharField(max_length=100, null=True)
    date_de_naissance = models.DateField(null=True)
    comeptence = ArrayField(models.CharField(max_length=24), blank=True, null=True, size=None)
    note = ArrayField(models.CharField(max_length=24), blank=True, null=True, size=None)


    def __str__(self):
        return self.mail
    def __str__(self):
        return self.nom_dept
class CompetenceModel(models.Model):
    code_comptence=models.CharField(max_length=20,null=True)
    competences = models.CharField(max_length=100, default=None)
class FormationModel(models.Model):
    name=models.CharField(max_length=100,null=True)
