# Generated by Django 4.2.18 on 2025-05-25 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_landingpage_is_fake'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='fake_landing_page_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
