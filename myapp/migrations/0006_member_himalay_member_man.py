# Generated by Django 5.0.4 on 2024-04-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_member_bank_ac_member_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='himalay',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='man',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]