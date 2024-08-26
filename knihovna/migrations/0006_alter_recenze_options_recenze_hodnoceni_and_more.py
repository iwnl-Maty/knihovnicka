# Generated by Django 5.0.3 on 2024-08-22 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knihovna', '0005_recenze'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recenze',
            options={'ordering': ['-hodnoceni'], 'verbose_name': 'Recenze', 'verbose_name_plural': 'Recenze'},
        ),
        migrations.AddField(
            model_name='recenze',
            name='hodnoceni',
            field=models.PositiveSmallIntegerField(choices=[(0, ''), (1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], default=5, verbose_name='hodnoceni knihy'),
        ),
        migrations.AddField(
            model_name='recenze',
            name='upraveno',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
