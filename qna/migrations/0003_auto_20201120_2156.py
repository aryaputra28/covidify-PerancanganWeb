# Generated by Django 3.1.2 on 2020-11-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0002_remove_pertanyaan_judul'),
    ]

    operations = [
        migrations.AddField(
            model_name='komentar',
            name='location',
            field=models.TextField(default='Depok', max_length=400),
        ),
        migrations.AddField(
            model_name='pertanyaan',
            name='location',
            field=models.TextField(default='Depok', max_length=400),
        ),
    ]