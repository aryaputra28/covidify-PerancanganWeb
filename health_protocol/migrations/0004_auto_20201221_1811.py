# Generated by Django 3.1.2 on 2020-12-21 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_pengguna_namalengkap'),
        ('health_protocol', '0003_auto_20201221_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternatives',
            name='pengguna',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='main.pengguna'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='alternatives',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='health_protocol.alternatives'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='pengguna',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='main.pengguna'),
        ),
    ]
