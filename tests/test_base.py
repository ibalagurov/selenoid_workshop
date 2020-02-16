import pytest
import allure


@pytest.mark.parametrize("browser_name,version", [("chrome", "80.0")])
@pytest.mark.parametrize("n", (_ for _ in range(12)))
def test_test(browser_name, version, selene_browser, n):

    browser = selene_browser(browser_name=browser_name, version=version)
    driver = browser.driver
    session_id = driver.session_id
    allure.attach(body=session_id, attachment_type=allure.attachment_type.TEXT, name="Session")

    with allure.step("Opening the page..."):
        browser.open("http://duckduckgo.com/")

    with allure.step("Typing search request..."):
        search_input = browser.element("input[id='search_form_input_homepage']")
        search_input.type("selenium").submit()

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
