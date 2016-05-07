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

    def __getitem__(self, idx):
        """
        Enables list-style access by index.
        """
        tabs = self._element.tabs
        if tabs is None:
            raise IndexError('TabStops object is empty')
        tab = tabs.tab_lst[idx]
        return TabStop(tab)

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

    @property
    def alignment(self):
        """
        A member of :ref:`WdTabAlignment` specifying the alignment setting
        for this tab stop.
        """
        return self._element.val

    @alignment.setter
    def alignment(self, value):
        self._element.val = value

    @property
    def leader(self):
        """
        A member of :ref:`WdTabLeader` specifying a repeating character used
        as a "leader", filling in the space spanned by this tab. Assigning
        |None| produces the same result as assigning `WD_TAB_LEADER.SPACES`.
        """
        return self._element.leader

    @leader.setter
    def leader(self, value):
        self._element.leader = value

    @property
    def position(self):
        """
        The distance (in EMU) of this tab stop from the inside edge of the
        paragraph. May be positive or negative.
        """
        return self._element.pos

    @position.setter
    def position(self, value):
        self._element.pos = value
