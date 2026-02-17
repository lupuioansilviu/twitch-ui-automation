Twitch Mobile UI Automation Framework

Design Principles
## Page Object Model (POM)
Each page encapsulates:
- Locators 
- UI interactions 
- Wait logic 
- Overlay handling

## Wait Strategy
The framework uses:
- WebDriverWait 
- Custom wait_loaded() logic 
- URL validation 
- DOM checks
Also, the framework includes:
  - retry logic
  - fallback navigation to directory page
  - element discovering 

## Chrome runs in mobile emulation mode:
options.add_experimental_option(
    "mobileEmulation",
    {"deviceName": "iPhone X"}
)

## Installation
 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

pytest3.9
Selenium
chrome WebDriver
Mobile Emulation

running tests - pytest -q 

taking screenshot - take_screenshot(driver, "streamer_page")


## Test cases
| Step | Action                 | Validation                         |
| ---- | ---------------------- | ---------------------------------- |
| 1    | Open Twitch            | Page loads successfully            |
| 2    | Click search icon      | Search input becomes available     |
| 3    | Search “StarCraft II”  | URL contains `/search?term=`       |
| 4    | Scroll twice           | Page scroll executes               |
| 5    | Click streamer         | Navigation away from search page   |
| 6    | Wait for streamer page | Key UI marker visible              |
| 7    | Screenshot             | Screenshot file saved successfully |


## NOTE for Dynamic UI

I noticed that Twitch app is very dynamic and rendering may not always complete consistently on the first interaction.
To improve that:
 - I have implemented that retries logic (e.g. clicking on the Browse)
 - accept cookies 
 - DOM readiness checks 
 - URL verification
 - for mobile emulation I am using iphoneX. I tried with newer version, but crashed 

## Note 2
Even tough I am not a fan to left locators in src/pages, I left them there to be visible and easy to find them


## Twitch Demo

Below is a recording of the test running locally:
- Opens Twitch
- Clicks search
- Search for *StarCraft II*
- Selects a streamer
- Waits for page load
- Takes screenshot
- Test passes successfully

![Twitch Mobile Test Demo](docs/twitchGif.gif)