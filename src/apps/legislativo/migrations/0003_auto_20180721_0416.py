# Generated by Django 2.0.4 on 2018-07-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislativo', '0002_auto_20180721_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laws',
            name='url_quechua',
            field=models.URLField(blank=True, null=True, verbose_name='Url pdf quechua'),
        ),
    ]