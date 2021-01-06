# Generated by Django 2.2.4 on 2020-08-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='alias',
            new_name='f_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='l_name',
        ),
        migrations.AddField(
            model_name='user',
            name='auth_level',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='desc',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
