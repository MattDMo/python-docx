# encoding: utf-8

"""
Tabstop-related proxy types.
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from ..shared import ElementProxy


class TabStops(ElementProxy):
    """
    A sequence providing access to the tab stops of a paragraph or paragraph
    style. Supports iteration, indexed access, del, and len(). It is accesed
    using the `tab_stops` property of ParagraphFormat; it is not intended to
    be constructed directly.
    """

    __slots__ = ()

    def __iter__(self):
        """
        Generate a TabStop object for each of the w:tab elements, in XML
        document order.
        """
        tabs = self._element.tabs
        if tabs is not None:
            for tab in tabs.tab_lst:
                yield TabStop(tab)

    def __len__(self):
        tabs = self._element.tabs
        if tabs is None:
            return 0
        return len(tabs.tab_lst)


class TabStop(ElementProxy):
    """
    An individual tab stop applying to a paragraph or style. Each of these is
    a member of a set held in a |TabStops| object.
    """

    __slots__ = ()
