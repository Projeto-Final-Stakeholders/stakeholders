# Generated by Django 4.2.2 on 2023-06-30 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholders', '0002_alter_formacao_tipo_oferta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portefolio',
            name='data_de_requisicao',
            field=models.DateField(auto_now_add=True),
        ),
    ]
