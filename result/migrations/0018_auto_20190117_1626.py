# Generated by Django 2.1.2 on 2019-01-17 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0017_auto_20190117_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='session',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='result.Session'),
        ),
    ]
