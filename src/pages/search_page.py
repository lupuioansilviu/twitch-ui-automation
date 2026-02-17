from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from src.core.base_page import BasePage


class SearchPage(BasePage):
    DIRECTORY_SEARCH_INPUT = (By.XPATH, "//input[@type='search' and (@placeholder='Search' or @data-a-target='tw-input')]")
    GENERIC_SEARCH_INPUT = (By.XPATH, "//input[@type='search']")

    def _find_search_input(self):
        try:
            return self.wait.until(lambda d: d.find_element(*self.DIRECTORY_SEARCH_INPUT))
        except TimeoutException:
            return self.wait.until(lambda d: d.find_element(*self.GENERIC_SEARCH_INPUT))

    def search(self, text: str):
        self.dismiss_overlays()

        try:
            inp = self._find_search_input()
        except TimeoutException:
            self.driver.refresh()
            self.dom_ready()
            self.dismiss_overlays()
            inp = self._find_search_input()

        inp.click()
        inp.clear()
        inp.send_keys(text)
        inp.send_keys(Keys.ENTER)

        self.wait.until(lambda d: "/search" in d.current_url and "term=" in d.current_url)


    def open_first_streamer_like_result(self):
        self.dismiss_overlays()

        candidate_xpath = (
            "//a[@href]"
            "[not(contains(@href,'/directory'))]"
            "[not(contains(@href,'/search'))]"
            "[not(contains(@href,'/downloads'))]"
            "[not(contains(@href,'/settings'))]"
            "[not(contains(@href,'/p/'))]"
        )

        def has_candidates(d):
            return len(d.find_elements(By.XPATH, candidate_xpath)) > 0

        self.wait.until(has_candidates)
        self.dismiss_overlays()

        links = self.driver.find_elements(By.XPATH, candidate_xpath)

        for a in links:
            href = (a.get_attribute("href") or "").strip()
            href_lower = href.lower()

            if not href:
                continue

            looks_like_channel = (
                    ("twitch.tv/" in href_lower) or
                    (href.startswith("/") and href.count("/") <= 2)
            )

            if not looks_like_channel:
                continue

            try:
                if a.is_displayed() and a.is_enabled():
                    a.click()
                    return
            except Exception:
                continue

        # click first visible candidate
        for a in links:
            try:
                if a.is_displayed() and a.is_enabled():
                    a.click()
                    return
            except Exception:
                pass

        raise TimeoutException("No clickable streamer link found on search results page")