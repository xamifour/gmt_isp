# Generated by Django 4.2.9 on 2024-07-01 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("openwisp_users", "0001_initial"),
        migrations.swappable_dependency(settings.OPENWISP_RADIUS_RADIUSGROUP_MODEL),
        ("gmtisp_billing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="openwisp_users.organization",
                verbose_name="organization",
            ),
        ),
        migrations.AddField(
            model_name="userplan",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="openwisp_users.organization",
                verbose_name="organization",
            ),
        ),
        migrations.AddField(
            model_name="userplan",
            name="plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.GMTISP_BILLING_PLAN_MODEL,
                verbose_name="plan",
            ),
        ),
        migrations.AddField(
            model_name="userplan",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
        migrations.AddField(
            model_name="recurringuserplan",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="openwisp_users.organization",
                verbose_name="organization",
            ),
        ),
        migrations.AddField(
            model_name="recurringuserplan",
            name="pricing",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="Recurring pricing",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.GMTISP_BILLING_PRICING_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="recurringuserplan",
            name="user_plan",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recurring",
                to=settings.GMTISP_BILLING_USERPLAN_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="quota",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="openwisp_users.organization",
                verbose_name="organization",
            ),
        ),
        migrations.AddField(
            model_name="pricing",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="openwisp_users.organization",
                verbose_name="organization",
            ),
        ),
        migrations.AddField(
            model_name="planquota",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="openwisp_users.organization",
                verbose_name="organization",
            ),
        ),
        migrations.AddField(
            model_name="planquota",
            name="plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.GMTISP_BILLING_PLAN_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="planquota",
            name="quota",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.GMTISP_BILLING_QUOTA_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="planpricing",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="openwisp_users.organization",
                verbose_name="organization",
            ),
        ),
        migrations.AddField(
            model_name="planpricing",
            name="plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.GMTISP_BILLING_PLAN_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="planpricing",
            name="pricing",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.GMTISP_BILLING_PRICING_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="planbandwidthsettings",
            name="bandwidth",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.GMTISP_BILLING_BANDWIDTHSETTINGS_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="planbandwidthsettings",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="openwisp_users.organization",
                verbose_name="organization",
            ),
        ),
        migrations.AddField(
            model_name="planbandwidthsettings",
            name="plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.GMTISP_BILLING_PLAN_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="plan",
            name="customized",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="customized:",
            ),
        ),
        migrations.AddField(
            model_name="plan",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="openwisp_users.organization",
                verbose_name="organization",
            ),
        ),
        migrations.AddField(
            model_name="plan",
            name="quotas",
            field=models.ManyToManyField(
                through="gmtisp_billing.PlanQuota",
                to=settings.GMTISP_BILLING_QUOTA_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="plan",
            name="radius_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plan_radius_group",
                to=settings.OPENWISP_RADIUS_RADIUSGROUP_MODEL,
                verbose_name="RADIUS group:",
            ),
        ),
        migrations.AddField(
            model_name="plan",
            name="temp_radius_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plan_temp_radius_group",
                to=settings.OPENWISP_RADIUS_RADIUSGROUP_MODEL,
                verbose_name="Temporary RADIUS group:",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="openwisp_users.organization",
                verbose_name="organization",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plan_order",
                to=settings.GMTISP_BILLING_PLAN_MODEL,
                verbose_name="plan",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="pricing",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.GMTISP_BILLING_PRICING_MODEL,
                verbose_name="pricing",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.GMTISP_BILLING_ORDER_MODEL,
                verbose_name="order",
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="openwisp_users.organization",
                verbose_name="organization",
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
        migrations.AddField(
            model_name="billinginfo",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="openwisp_users.organization",
                verbose_name="organization",
            ),
        ),
        migrations.AddField(
            model_name="billinginfo",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
        migrations.AddField(
            model_name="bandwidthsettings",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="openwisp_users.organization",
                verbose_name="organization",
            ),
        ),
        migrations.AddIndex(
            model_name="payment",
            index=models.Index(fields=["status"], name="gmtisp_bill_status_1d02c2_idx"),
        ),
        migrations.AddIndex(
            model_name="payment",
            index=models.Index(
                fields=["status", "transaction_id"],
                name="gmtisp_bill_status_1560a8_idx",
            ),
        ),
    ]