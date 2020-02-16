from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pytest


@pytest.mark.parametrize(
    "browser_name,version",
    [
        ("chrome", "80.0"),
        ("chrome", "79.0"),
        ("chrome", "78.0"),
        ("chrome", "77.0"),
        ("firefox", "71.0"),
        ("firefox", "72.0"),
        ("opera", "65.0"),
        ("opera", "66.0"),
    ],
)
def test_test(browser_name, version, request):
    capabilities = {
        "browserName": browser_name,
        "version": version,
        "platform": "LINUX",
        "enableVNC": True,
        "enableVideo": True,
        "enableLog": True,
        "name": f"{browser_name} {version} test - {request.node.name}",
        "screenResolution": "1024x768x24",
        "sessionTimeout": "2m",
    }
    driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=capabilities)

    try:
        print("Session ID is: %s" % driver.session_id)
        print("Opening the page...")
        driver.get("http://duckduckgo.com/")

        print("Typing search request...")
        search_input = driver.find_element_by_css_selector("input[id='search_form_input_homepage']")
        search_input.send_keys("selenium", Keys.ENTER)

        print("Taking screenshot...")
        driver.get_screenshot_as_file(f"screenshots/{driver.session_id}.png")
    finally:
        driver.quit()
