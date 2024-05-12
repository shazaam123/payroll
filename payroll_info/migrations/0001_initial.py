# Generated by Django 5.0.2 on 2024-05-11 14:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('payroll_history_id', models.AutoField(primary_key=True, serialize=False)),
                ('pay_date', models.DateField()),
                ('gross_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('net_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pay_method', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]