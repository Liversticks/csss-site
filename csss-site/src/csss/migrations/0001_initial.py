# Generated by Django 2.2.27 on 2023-01-03 18:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CronJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=5000, unique=True)),
                ('job_id', models.CharField(max_length=100, null=True, unique=True)),
                ('schedule', models.CharField(max_length=500)),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CronJobRunStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('run_time_in_seconds', models.IntegerField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csss.CronJob')),
            ],
        ),
    ]