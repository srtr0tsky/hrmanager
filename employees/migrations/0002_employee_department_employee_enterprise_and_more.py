# Generated by Django 4.1.6 on 2023-02-12 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enterprise', '0004_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ManyToManyField(to='department.department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='enterprise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='enterprise.enterprise'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
