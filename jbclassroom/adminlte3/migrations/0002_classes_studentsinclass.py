# Generated by Django 3.1.7 on 2021-03-11 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('className', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='StudentsInClass',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('classId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminlte3.classes')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminlte3.users')),
            ],
        ),
    ]
