# Generated by Django 3.0.4 on 2021-04-21 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_auto_20210420_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollows',
            name='follower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userfollows',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='followed', to=settings.AUTH_USER_MODEL),
        ),
    ]
