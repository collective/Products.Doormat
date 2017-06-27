# -*- coding: utf-8 -*-
from zope.interface import Interface


class IDoormat(Interface):
    """Marker interface for .Doormat.Doormat
    """


class IDoormatColumn(Interface):
    """Marker interface for .DoormatColumn.DoormatColumn
    """


class IDoormatSection(Interface):
    """Marker interface for .DoormatSection.DoormatSection
    """


class IDoormatReference(Interface):
    """Marker interface for .DoormatReference.DoormatReference
    """


class IDoormatLink(Interface):
    """Marker interface for .DoormatLink.DoormatLink
    """


class IDoormatMixin(Interface):
    """Marker interface for .DoormatMixin.DoormatMixin
    """


class IDoormatCollection(Interface):
    """Marker interface for .DoormatCollection.DoormatCollection
    """
