# Generated by Django 4.1.4 on 2022-12-28 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_card_data_week_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_data',
            name='week_image',
            field=models.FileField(default='test', upload_to=''),
        ),
    ]
