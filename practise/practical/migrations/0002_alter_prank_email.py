# Generated by Django 3.2.5 on 2021-07-28 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practical', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prank',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
