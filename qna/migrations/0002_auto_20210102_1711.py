# Generated by Django 3.1.2 on 2021-01-02 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentar',
            name='pengomentar',
            field=models.CharField(default='admin', max_length=400),
        ),
        migrations.AlterField(
            model_name='pertanyaan',
            name='penanya',
            field=models.CharField(default='admin', max_length=400),
        ),
    ]
