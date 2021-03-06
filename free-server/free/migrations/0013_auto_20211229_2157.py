# Generated by Django 3.2.9 on 2021-12-29 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0012_auto_20211118_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='apparatus',
            name='timeout',
            field=models.IntegerField(default=60, verbose_name='Connection timeout'),
        ),
        migrations.AddField(
            model_name='status',
            name='is_last',
            field=models.BooleanField(default=False, verbose_name='Is first?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='result',
            name='result_type',
            field=models.CharField(choices=[('f', 'Final'), ('p', 'Partial')], max_length=1, verbose_name='Result type'),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('online', 'Online'), ('hardware-error', 'Hardware error'), ('maintenance', 'Maintenance'), ('reserved', 'Reserved'), ('offline', 'Offline')], max_length=128, verbose_name='Status'),
        ),
    ]
