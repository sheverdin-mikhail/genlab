# Generated by Django 3.1 on 2021-03-03 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20201208_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerslid',
            name='page',
            field=models.CharField(choices=[('news', 'Новости'), ('about', 'О нас'), ('questions', 'Как сдать анализы'), ('researches', 'Исследования'), ('cooperation', 'Сотрудничество'), ('home', 'Главная страница')], default='home', max_length=50, verbose_name='Страница на которой отображать данный слайд'),
        ),
    ]
