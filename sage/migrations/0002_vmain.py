# Generated by Django 3.2 on 2021-05-10 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vmain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=40)),
                ('hname', models.CharField(max_length=40)),
                ('vname', models.CharField(max_length=69)),
                ('nov', models.FloatField(blank=True, default='', null=True)),
                ('vprice', models.FloatField(blank=True, default='', null=True)),
            ],
        ),
    ]
