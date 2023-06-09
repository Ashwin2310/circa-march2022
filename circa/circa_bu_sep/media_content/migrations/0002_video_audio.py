# Generated by Django 4.0.3 on 2022-04-14 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media_content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=200)),
                ('sub_theme', models.CharField(max_length=200)),
                ('caption', models.TextField(help_text='Enter a caption to be displayed with the image', max_length=1000)),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_content.theme')),
            ],
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=200)),
                ('sub_theme', models.CharField(max_length=200)),
                ('caption', models.TextField(help_text='Enter a caption to be displayed with the image', max_length=1000)),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_content.theme')),
            ],
        ),
    ]
