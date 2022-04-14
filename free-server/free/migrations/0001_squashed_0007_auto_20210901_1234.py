# Generated by Django 3.2.6 on 2021-09-01 10:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('free', '0001_initial'), ('free', '0002_result_execution'), ('free', '0003_auto_20210831_1710'), ('free', '0004_auto_20210901_1009'), ('free', '0005_auto_20210901_1036'), ('free', '0006_auto_20210901_1122'), ('free', '0007_auto_20210901_1234')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('name_en', models.CharField(max_length=64, null=True, verbose_name='Name')),
                ('name_pt', models.CharField(max_length=64, null=True, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_en', models.TextField(null=True, verbose_name='Description')),
                ('description_pt', models.TextField(null=True, verbose_name='Description')),
                ('config', models.JSONField(blank=True, default=dict, verbose_name='Configuration')),
                ('scientific_area', models.CharField(max_length=64, verbose_name='Scientific area')),
                ('scientific_area_en', models.CharField(max_length=64, null=True, verbose_name='Scientific area')),
                ('scientific_area_pt', models.CharField(max_length=64, null=True, verbose_name='Scientific area')),
                ('lab_type', models.CharField(max_length=32, verbose_name='Lab type')),
                ('lab_type_en', models.CharField(max_length=32, null=True, verbose_name='Lab type')),
                ('lab_type_pt', models.CharField(max_length=32, null=True, verbose_name='Lab type')),
            ],
            options={
                'verbose_name': 'Experiment',
                'verbose_name_plural': 'Experiments',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('name_en', models.CharField(max_length=64, null=True)),
                ('name_pt', models.CharField(max_length=64, null=True)),
                ('config', models.JSONField(blank=True, default=dict, verbose_name='Configuration')),
                ('experiment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='free.experiment')),
            ],
            options={
                'verbose_name': 'Protocol',
                'verbose_name_plural': 'Protocols',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Apparatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret', models.CharField(max_length=32, verbose_name='Secret')),
                ('owner', models.CharField(max_length=32, verbose_name='Owner')),
                ('experiment', models.ForeignKey(help_text='After setting/changing the experiment, press "Save and continue editing" to see the list of protocols.', on_delete=django.db.models.deletion.PROTECT, to='free.experiment')),
                ('location', models.CharField(default='', max_length=64, verbose_name='Location')),
                ('location_en', models.CharField(max_length=64, null=True, verbose_name='Location')),
                ('location_pt', models.CharField(max_length=64, null=True, verbose_name='Location')),
                ('protocols', models.ManyToManyField(blank=True, to='free.Protocol')),
            ],
            options={
                'verbose_name': 'Apparatus',
                'verbose_name_plural': 'Apparatuses',
                'ordering': ['location'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='Time')),
                ('status', models.CharField(choices=[('1', 'Online'), ('0', 'Offline'), ('R', 'Running')], max_length=1, verbose_name='Status')),
                ('apparatus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='free.apparatus')),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.CreateModel(
            name='Execution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config', models.JSONField(blank=True, default=dict, verbose_name='Configuration')),
                ('status', models.CharField(choices=[('R', 'Running'), ('E', 'Error'), ('C', 'Completed')], max_length=1, verbose_name='Status')),
                ('protocol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='free.protocol')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('apparatus', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='free.apparatus')),
                ('end', models.DateTimeField(default=datetime.datetime(2021, 9, 1, 10, 35, 56, 955092))),
                ('start', models.DateTimeField(default=datetime.datetime(2021, 9, 1, 10, 36, 2, 634987))),
            ],
            options={
                'verbose_name': 'Execution',
                'verbose_name_plural': 'Executions',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('s', 'Student'), ('t', 'Teacher'), ('a', 'Administrator')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='Time')),
                ('result_type', models.CharField(choices=[('p', 'Partial'), ('f', 'Final')], max_length=1, verbose_name='Result type')),
                ('value', models.JSONField(blank=True, default=dict, verbose_name='Value')),
                ('execution', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='free.execution')),
            ],
            options={
                'verbose_name': 'Result',
                'verbose_name_plural': 'Results',
            },
        ),
    ]
