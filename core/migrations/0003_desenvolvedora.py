# Generated by Django 3.2.7 on 2021-09-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210928_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desenvolvedora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
    ]