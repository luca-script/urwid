from __future__ import annotations

import doctest
import os
import unittest

import urwid
import urwid.numedit


def load_tests(loader: unittest.TestLoader, tests: unittest.BaseTestSuite, ignore) -> unittest.BaseTestSuite:
    module_doctests = [
        urwid.widget.attr_map,
        urwid.widget.attr_wrap,
        urwid.widget.bar_graph,
        urwid.widget.big_text,
        urwid.widget.box_adapter,
        urwid.widget.columns,
        urwid.widget.constants,
        urwid.widget.container,
        urwid.widget.divider,
        urwid.widget.edit,
        urwid.widget.filler,
        urwid.widget.frame,
        urwid.widget.grid_flow,
        urwid.widget.line_box,
        urwid.widget.overlay,
        urwid.widget.padding,
        urwid.widget.pile,
        urwid.widget.popup,
        urwid.widget.progress_bar,
        urwid.widget.solid_fill,
        urwid.widget.text,
        urwid.widget.widget,
        urwid.widget.widget_decoration,
        urwid.widget.wimp,
        urwid.display_common,
        urwid.event_loop.main_loop,
        urwid.numedit,
        urwid.monitored_list,
        urwid.raw_display,
        urwid.font,
        "urwid.split_repr",  # override function with same name
        urwid.util,
        urwid.signals,
    ]

    option_flags = doctest.ELLIPSIS | doctest.DONT_ACCEPT_TRUE_FOR_1 | doctest.IGNORE_EXCEPTION_DETAIL
    for m in module_doctests:
        tests.addTests(doctest.DocTestSuite(m, optionflags=option_flags))

    if os.name == "nt":
        tests.addTests(doctest.DocTestSuite("urwid._win32_raw_display", optionflags=option_flags))
    else:
        tests.addTests(doctest.DocTestSuite("urwid._posix_raw_display", optionflags=option_flags))
    return tests
