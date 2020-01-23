from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam213e', models.CharField(max_length=100, null=True)),
                ('specifications', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('price', django.contrib.postgres.fields.ranges.FloatRangeField(null=True)),
            ],
        ),
    ]