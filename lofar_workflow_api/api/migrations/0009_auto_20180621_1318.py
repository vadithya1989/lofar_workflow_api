# Generated by Django 2.0.4 on 2018-06-21 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20180621_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='avg_freq_step',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='session',
            name='avg_time_step',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='session',
            name='demix_freq_step',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='session',
            name='demix_sources',
            field=models.CharField(choices=[('CasA', 'CasA'), ('CygA', 'CygA')], default='CasA', max_length=4),
        ),
        migrations.AddField(
            model_name='session',
            name='demix_time_step',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='session',
            name='do_demix',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='session',
            name='parset',
            field=models.CharField(choices=[('', ''), ('hba_npp', 'hba_npp'), ('hba_raw', 'hba_raw'), ('lba_npp', 'lba_npp'), ('lba_raw', 'lba_raw')], default='lba_npp', max_length=7),
        ),
        migrations.AddField(
            model_name='session',
            name='select_NL',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='session',
            name='status',
            field=models.CharField(choices=[('unknown', 'unknown'), ('running', 'running'), ('finished', 'finished')], default='unknown', max_length=20),
        ),
    ]
