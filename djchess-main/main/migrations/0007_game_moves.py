# Generated by Django 4.2.16 on 2024-10-21 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_game_journal_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='moves',
            field=models.TextField(blank=True, null=True),
        ),
    ]
