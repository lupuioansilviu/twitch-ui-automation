from src.pages.home_page import HomePage
from src.pages.search_page import SearchPage
from src.pages.streamer_page import StreamerPage
from src.utils.artifacts import take_screenshot


def test_twitch_mobile_search_and_open_streamer(driver):
    home = HomePage(driver)
    search = SearchPage(driver)
    streamer = StreamerPage(driver)

# 1) access Twitch app
    home.open()
    home.dom_ready()
    home.dismiss_overlays()

# 2) click the search icon
    home.open_search()
    home.dismiss_overlays()

# 3) input StarCraft II
    search.search("StarCraft II")
    home.dom_ready()
    home.dismiss_overlays()

# 4) scroll down 2 times
    home.scroll_down(times=2)

# 5) select one streamer
    search.open_first_streamer_like_result()

# 6) streamer page: wait until loaded and take screenshot
    streamer.wait_loaded()
    home.dismiss_overlays()

    path = take_screenshot(driver, "streamer_page")
    assert path