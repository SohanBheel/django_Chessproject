# Generated by Django 4.2.16 on 2024-10-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_gameinvitation_delete_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('waiting_for_player', 'Waiting for Player'), ('in_progress', 'In Progress'), ('over', 'Over')], default='waiting_for_player', max_length=20),
        ),
        migrations.DeleteModel(
            name='GameInvitation',
        ),
    ]
