# Generated by Django 4.1.7 on 2023-05-16 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxymodelapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('proxymodelapp.useraccount',),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('proxymodelapp.useraccount',),
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='is_student',
            new_name='is_doctor',
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='is_teacher',
            new_name='is_patient',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='type',
            field=models.CharField(choices=[('PATIENT', 'patient'), ('DOCTOR', 'doctor')], default='PATIENT', max_length=8),
        ),
    ]
