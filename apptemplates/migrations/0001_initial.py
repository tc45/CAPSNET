# Generated by Django 3.1.2 on 2020-10-20 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(help_text='Group name', max_length=100)),
                ('description', models.CharField(blank=True, help_text='Description', max_length=100)),
                ('deleted', models.BooleanField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(blank=True, null=True)),
                ('deleted', models.BooleanField(blank=True)),
                ('group', models.ForeignKey(help_text='Template Group', on_delete=django.db.models.deletion.PROTECT, to='apptemplates.templategroup', verbose_name='Template Group')),
            ],
        ),
    ]
