# Generated by Django 4.0.4 on 2022-05-23 23:39

import contextlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(blank=True, choices=[('computer science', 'COMPUTER SCIENCE'), ('information system', 'INFORMATION SYSTEM'), ('information technology', 'INFORMATION TECHNOLOGY'), ('artificial intelligence', 'ARTIFICIAL INTELLIGENCE'), ('decision support system', 'DECISION SUPPORT SYSTEM'), ('null', 'NULL')], default=contextlib.nullcontext, max_length=32, null=True),
        ),
    ]