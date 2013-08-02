from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext as _
from django.contrib import admin
from models import NavigationList, NavigationListItem
from forms import NavigationListForm


class NavigationListItemInline(admin.TabularInline):
    model = NavigationListItem
    extra = 1

class NavigationListPlugin(CMSPluginBase):

    model = NavigationList
    name = _("Navigation List")
    module = "Navigation"
    render_template = "navigation_list.html"
    form = NavigationListForm

    inlines = [NavigationListItemInline]

    def render(self, context, instance, placeholder):
        context.update({'instance' : instance})
        return context

plugin_pool.register_plugin(NavigationListPlugin)
