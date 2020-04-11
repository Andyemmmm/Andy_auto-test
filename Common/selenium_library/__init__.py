from Common.selenium_library.browser import Browser

from Common.selenium_library.element import Element
from Common.selenium_library.window import Window


class SeleniumBase(Browser, Element, Window):
    """封装Selenium基本操作"""
    pass
