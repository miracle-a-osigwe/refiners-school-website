# Generated by Django 5.0.4 on 2024-05-04 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_updateimage_img_use'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateimage',
            name='img_tag',
            field=models.CharField(max_length=200, verbose_name='Image description'),
        ),
        migrations.AlterField(
            model_name='updateimage',
            name='img_use',
            field=models.IntegerField(choices=[(1, 'gallery'), (2, 'homepage'), (3, 'all'), (4, 'labs'), (5, 'reception'), (6, 'nursery/primary'), (7, 'secondary'), (8, 'classes'), (9, 'workshops')], default=3, verbose_name='Page image assignment'),
        ),
    ]
