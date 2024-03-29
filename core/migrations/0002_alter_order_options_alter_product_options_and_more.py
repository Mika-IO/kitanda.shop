# Generated by Django 4.2.4 on 2023-10-04 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"verbose_name": "Pedido", "verbose_name_plural": "Pedidos"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Produto", "verbose_name_plural": "Produtos"},
        ),
        migrations.AlterModelOptions(
            name="store",
            options={"verbose_name": "Loja", "verbose_name_plural": "Lojas"},
        ),
        migrations.AlterField(
            model_name="order",
            name="content",
            field=models.TextField(verbose_name="Conteúdo"),
        ),
        migrations.AlterField(
            model_name="order",
            name="delivery_fee",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=10,
                verbose_name="Taxa de Entrega",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("pendente", "Pendente"),
                    ("preparando", "Preparando"),
                    ("em_entrega", "Em Entrega"),
                    ("concluido", "Concluído"),
                ],
                default="pendente",
                max_length=20,
                verbose_name="Status",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="store",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.store",
                verbose_name="Loja",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="subtotal",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, verbose_name="Subtotal"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="total",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, verbose_name="Total"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(verbose_name="Descrição"),
        ),
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="produtos/", verbose_name="Imagem"),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Nome"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Preço"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="store",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.store",
                verbose_name="Loja",
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="UF",
            field=models.CharField(
                blank=True, default="RO", max_length=2, null=True, verbose_name="Estado"
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="address",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Endereço"
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="city",
            field=models.CharField(
                blank=True,
                default="Ariquemes",
                max_length=100,
                null=True,
                verbose_name="Cidade",
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="delivery_fee",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=10,
                verbose_name="Taxa de Entrega",
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="facebook",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Facebook"
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="image",
            field=models.ImageField(upload_to="lojas/", verbose_name="Imagem"),
        ),
        migrations.AlterField(
            model_name="store",
            name="instagram",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Instagram"
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="name",
            field=models.CharField(max_length=100, unique=True, verbose_name="Nome"),
        ),
        migrations.AlterField(
            model_name="store",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Proprietário",
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="slug",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Slug"
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="type",
            field=models.CharField(
                choices=[
                    ("mercado", "Mercado"),
                    ("farmacia", "Farmácia"),
                    ("frutaria", "Frutaria"),
                    ("outro", "Outro"),
                ],
                max_length=20,
                verbose_name="Tipo",
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="whatsapp",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="WhatsApp"
            ),
        ),
        migrations.AlterModelTable(
            name="order",
            table="core_order",
        ),
        migrations.AlterModelTable(
            name="product",
            table="core_product",
        ),
        migrations.AlterModelTable(
            name="store",
            table="core_store",
        ),
    ]
