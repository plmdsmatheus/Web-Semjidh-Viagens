from django.db import migrations

def preencher_veiculo_padrao(apps, schema_editor):
    Viagem = apps.get_model('semjidhapp', 'Viagem')
    Viagem.objects.filter(veiculo__isnull=True).update(veiculo='Carro (4 lugares)')

class Migration(migrations.Migration):
    dependencies = [
        ('semjidhapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(preencher_veiculo_padrao),
    ]