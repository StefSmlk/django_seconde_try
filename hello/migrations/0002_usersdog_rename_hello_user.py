# Generated by Django 5.1.1 on 2024-09-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersDog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('breed', models.CharField(max_length=30, verbose_name='Порода')),
                ('is_bought', models.BooleanField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Hello',
            new_name='User',
        ),
    ]