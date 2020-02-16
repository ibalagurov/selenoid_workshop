from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pytest
import allure

GGR = True

host = "http://test:test-password@localhost:4445/wd/hub" if GGR else "http://localhost:4444/wd/hub"


@pytest.mark.parametrize(
    "browser_name,version",
    [
        ("chrome", "80.0"),
        ("chrome", "80.0"),
        ("chrome", "80.0"),
        ("chrome", "80.0"),
        ("chrome", "80.0"),
        ("chrome", "80.0"),
        ("chrome", "79.0"),
        ("firefox", "71.0"),
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
    driver = webdriver.Remote(command_executor=host, desired_capabilities=capabilities)

    try:
        session_id = driver.session_id
        allure.attach(body=session_id, attachment_type=allure.attachment_type.TEXT)
        print(f"Session ID is: {session_id}")
        print("Opening the page...")
        driver.get("http://duckduckgo.com/")

        print("Typing search request...")
        search_input = driver.find_element_by_css_selector("input[id='search_form_input_homepage']")
        search_input.send_keys("selenium", Keys.ENTER)

        print("Taking screenshot...")
        driver.get_screenshot_as_file(f"screenshots/{session_id}.png")
        allure.link(url=f"http://localhost:4445/host/{session_id}", name="host")
        allure.link(url=f"http://localhost:4445/logs/{session_id}", name="logs")
        allure.link(url=f"http://localhost:4445/video/{session_id}", name="video")
    finally:
        driver.quit()
