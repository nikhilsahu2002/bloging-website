# Generated by Django 4.2.1 on 2023-07-20 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0013_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='Login.newsarticle'),
        ),
    ]