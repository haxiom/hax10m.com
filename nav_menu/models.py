from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.models.fields import PageField

class NavigationList(CMSPlugin):
    css_class = models.CharField(max_length=100, default="nav")

    def copy_relations(self, oldinstance):
        for item in oldinstance.navigationlistitem_set.all():
            item.pk = None
            item.navigation_list = self
            item.save()

class NavigationListItem(models.Model):
    navigation_list = models.ForeignKey(NavigationList)
    name = models.CharField(_("name"), max_length=255)
    image = models.ImageField(upload_to="uploads/", blank=True)
    url = models.URLField(null=True, blank=True)
    page_link = PageField(null=True, blank=True)
    target = models.CharField(_("target"), blank=True, max_length=64, choices=((
        ("", _("same window")),
        ("_blank", _("new window")),
        ("_parent", _("parent window")),
        ("_top", _("topmost frame")),
    )))
    order = models.IntegerField(null=True, blank=True)

    def get_link(self):
        result = None
        if self.page_link != None:
            result = self.page_link.get_absolute_url()
        elif self.url != None:
            result = self.url
        return result

    def save(self, *args, **kwargs):
        if self.order is None:
            list_items = NavigationListItem.objects.filter(navigation_list=self.navigation_list).reverse()
            if list_items:
                self.order = list_items[0].order + 1
            else:
                self.order = 1
        super(NavigationListItem, self).save(*args, **kwargs)


    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.name
