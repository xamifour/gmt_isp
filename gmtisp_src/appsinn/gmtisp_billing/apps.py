import logging
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

from openwisp_utils.admin_theme.menu import register_menu_group
# from openwisp_utils.api.apps import ApiAppConfig
from swapper import get_model_name

from . import conf as app_settings
logger = logging.getLogger(__name__)


class GmtispBillingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gmtisp_billing'
    label = 'gmtisp_billing'
    # verbose_name = _('Subscriptions')
    verbose_name = _(app_settings.APP_VERBOSE_NAME)

    def ready(self):
        # noinspection PyUnresolvedReferences
        import gmtisp_billing.listeners  # noqa
        self.register_menu_group()

    def register_menu_group(self):
        items = {
            1: {
                'label': _('Plans'),
                'model': get_model_name(self.label, 'Plan'),
                'name': 'changelist',
                'icon': 'ow-radius-accounting',
            },
            2: {
                'label': _('Orders'),
                'model': get_model_name(self.label, 'Order'),
                'name': 'changelist',
                'icon': 'ow-radius-checks',
            },
            3: {
                'label': _('Invoices'),
                'model': get_model_name(self.label, 'Invoice'),
                'name': 'changelist',
                'icon': 'ow-radius-nas',
            },
            # 4: {
            #     'label': _('Payments'),
            #     'model': get_model_name(self.label, 'Payment'),
            #     'name': 'changelist',
            #     'icon': 'ow-radius-checks',
            # },

        }
        register_menu_group(
            position=23,
            config={'label': _('Subscriptions'), 'items': items, 'icon': 'ow-radius'},
        )


# del PlansConfig
# del ApiAppConfig