# Generated by Django 3.1.7 on 2021-04-01 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('principal', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.PositiveIntegerField()),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='basic_app.school')),
            ],
        ),
    ]
