# Generated by Django 4.1.6 on 2023-02-12 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_user'),
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee'),
        ),
    ]
