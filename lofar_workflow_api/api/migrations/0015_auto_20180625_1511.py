# Generated by Django 2.0.4 on 2018-06-25 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20180625_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='status',
            field=models.CharField(choices=[('unknown', 'unknown'), ('started', 'started'), ('failure', 'failure')], default='unknown', max_length=20),
        ),
    ]
