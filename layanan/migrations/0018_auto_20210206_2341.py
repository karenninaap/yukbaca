# Generated by Django 2.2 on 2021-02-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layanan', '0017_auto_20210206_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='judul',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='repository',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=200),
        ),
    ]
