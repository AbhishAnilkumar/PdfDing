# Generated by Django 5.0.6 on 2024-07-11 10:44

import django.db.models.deletion
import pdf.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_remove_unnecessary_profile_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('file', models.FileField(upload_to=pdf.models.get_file_path)),
                ('description', models.TextField(blank=True, help_text='Optional', null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('current_page', models.IntegerField(default=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('tags', models.ManyToManyField(blank=True, to='pdf.tag')),
            ],
        ),
    ]
