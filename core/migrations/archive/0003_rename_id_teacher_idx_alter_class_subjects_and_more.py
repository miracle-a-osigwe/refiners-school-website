# Generated by Django 5.0.4 on 2024-04-30 22:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_home_schoolvision_aboutus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='id',
            new_name='idx',
        ),
        migrations.AlterField(
            model_name='class',
            name='subjects',
            field=models.ManyToManyField(related_name='class_subjects', to='core.subject', verbose_name='Subjects'),
        ),
        migrations.AlterField(
            model_name='home',
            name='author',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='subject',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_subjects', to='core.section', verbose_name='Section'),
        ),
    ]