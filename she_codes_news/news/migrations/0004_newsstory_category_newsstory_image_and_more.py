# Generated by Django 4.0.1 on 2022-02-15 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_alter_newsstory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='category',
            field=models.CharField(choices=[('TRAVELS', 'Travels'), ('CODING', 'Coding'), ('MISC', 'Misc')], default='Misc', max_length=200),
        ),
        migrations.AddField(
            model_name='newsstory',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsstory',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to=settings.AUTH_USER_MODEL),
        ),
    ]
