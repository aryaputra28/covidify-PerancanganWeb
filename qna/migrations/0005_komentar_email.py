# Generated by Django 3.1.2 on 2020-12-19 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0004_pertanyaan_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='komentar',
            name='email',
            field=models.EmailField(default='gilang.catur@ui.ac.id', max_length=254),
        ),
    ]