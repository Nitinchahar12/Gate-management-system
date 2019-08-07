# Generated by Django 2.2.4 on 2019-08-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry_Exit',
            fields=[
                ('name', models.TextField(blank=True, null=True)),
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('dob', models.DateField(verbose_name='Date')),
                ('gate_entry_number', models.IntegerField(blank=True, null=True)),
                ('entry_timestamp', models.DateTimeField(blank=True, null=True)),
                ('exit_timestamp', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Entry Exit',
                'verbose_name_plural': 'Entry Exit',
            },
        ),
    ]