# Generated by Django 2.2 on 2021-02-06 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layanan', '0012_auto_20210204_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='katalog_jurusan',
            field=models.CharField(choices=[('psikologi', 'Psikologi'), ('informatika', 'Informatika'), ('teknik mesin', 'Teknik Mesin'), ('teknik elektro', 'Teknik Elektro'), ('kedokteran', 'Kedokteran'), ('farmasi', 'Farmasi'), ('biologi', 'Biologi'), ('fisika', 'Fisika'), ('ekonomi', 'Ekonomi'), ('akuntansi', 'Akuntansi'), ('pendidikan guru sekolah dasar', 'Pendidikan Guru Sekolah Dasar'), ('sastra indonesia', 'Sasta Indonesia'), ('sastra inggris', 'Sastra Inggris'), ('ilmu politik', 'Ilmu Politik')], default='psikologi', max_length=200),
        ),
    ]
