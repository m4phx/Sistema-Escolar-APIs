# Generated by Django 3.2.5 on 2021-11-03 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('carga_horaria', models.CharField(max_length=3)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.curso')),
            ],
        ),
    ]
