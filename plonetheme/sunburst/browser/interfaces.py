from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer


class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope browser layer.
    """


class ISunburstView(Interface):
    """ """

    def getColumnsClass():
        """Returns the CSS class for column content based on columns presence.
        """

    def getColumnsClasses():
        """Returns all CSS classes based on columns presence.
        """
