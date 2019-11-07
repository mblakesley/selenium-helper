from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

import custom_conditions as CC


class WebElementPlus(WebElement):
    """Represents a DOM element. Extends the parent class to add a few methods."""
    def __init__(self, web_element):
        """
        Constructor. Overrides the parent method to accept an object instead of a set of attributes

        Args:
            web_element (Selenium WebElement object): element object, generated by Selenium find_*() methods
        """
        super().__init__(web_element._parent, web_element._id, web_element._w3c)

    def replace_text(self, *value):
        """
        Replace the current text in the element

        Args:
            *value (str): string(s) to replace the current text
        """
        self.clear()
        self.send_keys(*value)

    def click(self, wait=10):
        """
        Wait until the element is clickable, then click it

        Args:
            wait (int, optional): max number of seconds to wait. Defaults to 10.

        Returns:
            WebElementPlus object: the element itself. Useful for simultaneously clicking & storing the element
        """
        WebDriverWait(self._parent, wait).until(CC.element_to_be_clickable(self))
        super().click()
        return self

    # TODO: 'should' methods - if we have to write our own asserts over for pytest, might as well
    # TODO: value property
