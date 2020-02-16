from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pytest
import allure

GGR = True

host = "http://test:test-password@localhost:4445/wd/hub" if GGR else "http://localhost:4444/wd/hub"


@pytest.mark.parametrize(
    "browser_name,version", [("chrome", "80.0")],
)
@pytest.mark.parametrize("n", (_ for _ in range(24)))
def test_test(browser_name, version, request, n):
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
        allure.attach(body=session_id, attachment_type=allure.attachment_type.TEXT, name="Session")

        with allure.step("Opening the page..."):
            driver.get("http://duckduckgo.com/")

        with allure.step("Typing search request..."):
            search_input = driver.find_element_by_css_selector("input[id='search_form_input_homepage']")
            search_input.send_keys("selenium", Keys.ENTER)

        with allure.step("Taking screenshot..."):
            screen_shot = driver.get_screenshot_as_png()
            allure.attach(body=screen_shot, attachment_type=allure.attachment_type.PNG)

        allure.attach(
            body=f"http://localhost:4445/host/{session_id}",
            attachment_type=allure.attachment_type.TEXT,
            name="Host information",
        )
        allure.attach(
            body=f"http://localhost:4445/logs/{session_id}",
            attachment_type=allure.attachment_type.TEXT,
            name="Selenium logs",
        )
        allure.attach(
            body=f"http://localhost:4445/video/{session_id}", attachment_type=allure.attachment_type.TEXT, name="Video"
        )
    finally:
        driver.quit()
