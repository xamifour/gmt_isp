# Generated by Django 5.1.3 on 2024-11-17 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openwisp_users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='location',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='session_quota',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='theme',
        ),
        migrations.RemoveField(
            model_name='user',
            name='theme',
        ),
        migrations.AlterField(
            model_name='organization',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(help_text='The name of the organization', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='notes',
            field=models.TextField(blank=True, help_text='notes for internal usage', verbose_name='notes'),
        ),
    ]