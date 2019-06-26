# Generated by Django 2.2.2 on 2019-06-24 15:02

from django.db import migrations
from django.conf import settings
import os
import csv


def load_initial_questions(apps, schema_editor):
    Stack = apps.get_model('core', 'Stack')
    Card = apps.get_model('core', 'Card')

    Card.objects.all().delete()
    Stack.objects.all().delete()

    stack = Stack(name="Python")
    stack.save()

    filename = os.path.join(settings.BASE_DIR, 'cards.csv')

    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            card = Card(prompt=row['prompt'], answer=row['answer'], stack=stack)
            card.save()


def delete_data(apps, schema_editor):
    Stack = apps.get_model('core', 'Stack')
    Card = apps.get_model('core', 'Card')

    Card.objects.all().delete()
    Stack.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190624_1448'),
    ]

    operations = [migrations.RunPython(load_initial_questions, delete_data)]