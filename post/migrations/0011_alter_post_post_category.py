# Generated by Django 5.0.4 on 2024-05-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_post_post_category_alter_post_img_alter_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_category',
            field=models.IntegerField(choices=[(1, 'about us summary'), (2, 'mission'), (3, 'vision'), (4, 'event'), (5, 'about us full'), (6, 'offer'), (7, 'creed'), (8, 'core values'), (9, 'school anthem')], default=4, verbose_name='Post category'),
        ),
    ]
