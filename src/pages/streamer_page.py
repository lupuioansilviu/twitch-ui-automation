from selenium.webdriver.common.by import By
from src.core.base_page import BasePage


class StreamerPage(BasePage):
    " left locators here as well, even tough they need to be moved into a separate folder"
    LOADED_MARKERS = [
        (By.XPATH, "//*[@data-a-target='follow-button']"),
        (By.XPATH, "//button[contains(.,'Follow')]"),
        (By.XPATH, "//main"),
        (By.XPATH, "//video"),
    ]

    def wait_loaded(self):
        self.dom_ready()

        self.wait.until(lambda d: "/search" not in d.current_url and "/directory" not in d.current_url)

        self.dismiss_overlays()

        def any_marker_present(d):
            for loc in self.LOADED_MARKERS:
                if d.find_elements(*loc):
                    return True
            return False

        self.wait.until(any_marker_present)

        self.dismiss_overlays()

    def dismiss_popups(self):
        self.dismiss_overlays()