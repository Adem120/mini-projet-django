# Generated by Django 4.1.2 on 2022-12-10 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0002_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(max_length=20)),
                ('datedebut', models.DateField()),
                ('datefin', models.DateField()),
            ],
        ),
    ]
