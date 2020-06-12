# Generated by Django 3.0.3 on 2020-02-27 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('econtact', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]