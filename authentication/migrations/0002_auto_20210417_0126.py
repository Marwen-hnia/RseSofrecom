# Generated by Django 2.2.10 on 2021-04-17 00:26

from django.db import migrations, models
import django_postgres_extensions.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Telephone_personnel',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Telephone_professionnel',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='adate',
            field=django_postgres_extensions.models.fields.ArrayField(base_field=models.CharField(max_length=24), blank=True,  null=True, size=None),
        ),
        migrations.AddField(
            model_name='user',
            name='adresse_domicile',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='adresse_residence',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='certification',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date_de_naissance',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='datede',
            field=django_postgres_extensions.models.fields.ArrayField(base_field=models.CharField(max_length=24), blank=True,  null=True, size=None),
        ),
        migrations.AddField(
            model_name='user',
            name='formation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='post',
            field=django_postgres_extensions.models.fields.ArrayField(base_field=models.CharField(max_length=24), blank=True,  null=True, size=None),
        ),
        migrations.AddField(
            model_name='user',
            name='vie_associative',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
