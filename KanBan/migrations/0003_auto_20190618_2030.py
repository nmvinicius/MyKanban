# Generated by Django 2.2.2 on 2019-06-19 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KanBan', '0002_tarefa_dtprazo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='dtstatus',
            new_name='dtcriacao',
        ),
    ]