from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from src.core.base_page import BasePage


class HomePage(BasePage):
    URL = "https://www.twitch.tv/"
    BROWSE = (By.XPATH, "//*[normalize-space()='Browse']")

    def open(self):
        self.driver.get(self.URL)
        self.dom_ready()
        self.dismiss_overlays()

    def _directory_loaded(self, d) -> bool:
        return (
            "/directory" in d.current_url
            or len(d.find_elements(By.XPATH, "//input[@type='search']")) > 0
        )

    def go_to_directory(self):
        self.dismiss_overlays()

        # Try clicking msx 3 times
        for _ in range(3):
            try:
                self.click_with_overlay_handling(self.BROWSE)
                self.wait.until(self._directory_loaded)
                self.dom_ready()
                self.dismiss_overlays()
                return
            except TimeoutException:
                self.dismiss_overlays()

        try:
            self.driver.refresh()
            self.dom_ready()
            self.dismiss_overlays()
            self.click_with_overlay_handling(self.BROWSE)
            self.wait.until(self._directory_loaded)
            self.dom_ready()
            self.dismiss_overlays()
            return
        except TimeoutException:
            pass

        self.driver.get("https://m.twitch.tv/directory")
        self.dom_ready()
        self.dismiss_overlays()
        self.wait.until(self._directory_loaded)

    def open_search(self):
        self.go_to_directory()
        self.dismiss_overlays()

        search_input_xpath = "//input[@type='search']"

        for _ in range(3):
            try:
                el = self.wait.until(lambda d: d.find_element(By.XPATH, search_input_xpath))
                try:
                    el.click()
                except Exception:
                    self.driver.execute_script("arguments[0].click();", el)
                return
            except TimeoutException:
                self.dismiss_overlays()

        raise TimeoutException("Could not click the search input")