# Generated by Django 3.1.2 on 2020-11-03 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Snus', '0002_produt_listnummer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produt',
            name='Img',
            field=models.ImageField(default='default.png', upload_to='SnusBildere'),
        ),
    ]
