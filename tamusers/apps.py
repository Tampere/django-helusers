from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TunnistamoUsersConfig(AppConfig):
    name = 'tamusers'
    verbose_name = _("Tunnistamo Users")
