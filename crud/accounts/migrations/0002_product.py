# Generated by Django 3.1.7 on 2021-03-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(max_length=12)),
                ('category', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('date_create', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
