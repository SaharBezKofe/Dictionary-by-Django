# Generated by Django 4.0.4 on 2022-06-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0010_alter_runword_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='runword',
            name='user_answer',
            field=models.CharField(default='', max_length=200, verbose_name='Ответ пользователя'),
        ),
    ]