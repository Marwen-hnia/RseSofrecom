# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from authentication.models import User, CompetenceModel, FormationModel


@admin.register(User)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('mat_emp', 'nom_emp', 'mail', 'nom_dept', 'nom_resp', 'nom_dept_parent',
     'name_bu', 'name_direction', 'resp_bu', 'mail', 'nb_exp', 'seniorite'
    ,'adresse_residence','adresse_domicile','Telephone_professionnel','Telephone_personnel',
    'linkedin','post','datede','adate','formation','certification','vie_associative','date_de_naissance','comeptence','note')
@admin.register(CompetenceModel)
class ViewAdmin(ImportExportModelAdmin):
    list_display=('code_comptence','competences')
@admin.register(FormationModel)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['name']