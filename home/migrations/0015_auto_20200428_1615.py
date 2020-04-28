# Generated by Django 2.1.15 on 2020-04-28 16:15

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0014_auto_20190627_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='corespage',
            name='second_block_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='first_block_credits',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Texto 1'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='first_block_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='second_block_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='second_block_text',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Créditos da imagem'),
        ),
    ]
