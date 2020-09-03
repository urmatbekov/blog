# Generated by Django 3.1 on 2020-09-03 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_expiring_token', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expiringtoken',
            options={'verbose_name': 'Токен', 'verbose_name_plural': 'Токены'},
        ),
        migrations.AlterField(
            model_name='expiringtoken',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='expiringtoken',
            name='key',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Ключ'),
        ),
        migrations.AlterField(
            model_name='expiringtoken',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]