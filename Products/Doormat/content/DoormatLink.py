# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.Archetypes import atapi
from Products.ATContentTypes.content.link import ATLinkSchema, ATLink
from zope.interface import implements
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.Doormat.config import PROJECTNAME
from Products.Doormat import DoormatMF as _

import interfaces

schema = atapi.Schema((

    atapi.BooleanField(
        name='open_in_new_window',
        widget=atapi.BooleanField._properties['widget'](
            label=_(u"Open in new window?"),
            description=_(u"Open this link in a new browser window or tab"),
            label_msgid='Doormat_label_openInNewWindow',
            description_msgid='Doormat_help_openInNewWindow',
            i18n_domain='Doormat',
        ),
    ),
),
)

DoormatLink_schema = ATLinkSchema.copy() + \
    schema.copy()


class DoormatLink(ATLink, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IDoormatLink)

    meta_type = 'DoormatLink'
    _at_rename_after_creation = True

    schema = DoormatLink_schema


atapi.registerType(DoormatLink, PROJECTNAME)
