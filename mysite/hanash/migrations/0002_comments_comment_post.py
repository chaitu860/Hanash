# Generated by Django 4.0.2 on 2022-04-10 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hanash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_img', to='hanash.posts'),
            preserve_default=False,
        ),
    ]