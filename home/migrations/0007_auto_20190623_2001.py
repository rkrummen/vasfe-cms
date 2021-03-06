# Generated by Django 2.1.2 on 2019-06-23 23:01

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0006_auto_20190622_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='StdPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('first_block', models.CharField(max_length=255, verbose_name='Titulo do primeiro bloco')),
                ('first_block_text', wagtail.core.fields.RichTextField(blank=True, verbose_name='Texto 1')),
                ('second_block', models.CharField(max_length=255, verbose_name='Titulo do segundo bloco')),
                ('second_block_text', wagtail.core.fields.RichTextField(blank=True, verbose_name='Texto 1')),
                ('third_block', models.CharField(max_length=255, verbose_name='Titulo do terceiro bloco')),
                ('third_block_text', wagtail.core.fields.RichTextField(blank=True, verbose_name='Texto 1')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='second_block',
            field=models.CharField(max_length=255, verbose_name='Titulo do segundo bloco'),
        ),
    ]
