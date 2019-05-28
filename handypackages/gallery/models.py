from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField

from handypackages.tag.models import Tag


class GalleryAbstractModel(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('Title')
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        on_delete=models.CASCADE
    )
    text = RichTextUploadingField(
        verbose_name=_('Text')
    )
    tags = models.ManyToManyField(Tag)
    create_time = models.DateTimeField(
        verbose_name=_('Time Create'),
        editable=False,
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title

    @property
    def gallery_tags(self):
        """ will return all gallery tags """
        return self.tags.all()

    class Meta:
        abstract = True
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')


class Gallery(GalleryAbstractModel):
    """
    Gallery model.
    if you don't like this model, inherite GalleryAbstractModel
    and overwite it
    """