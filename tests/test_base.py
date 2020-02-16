from selenium import webdriver
from selenium.webdriver.common.keys import Keys

capabilities = {
    "browserName": "chrome",
    "version": "80.0",
    "platform": "LINUX",
    # "enableVNC": True,
    # "enableVideo": True,
}


def test_test():
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=capabilities
    )

    try:
        print('Session ID is: %s' % driver.session_id)
        print('Opening the page...')
        driver.get('http://duckduckgo.com/')

        print('Typing search request...')
        search_input = driver.find_element_by_css_selector(
            "input[id='search_form_input_homepage']")
        search_input.send_keys("selenium", Keys.ENTER)

        print('Taking screenshot...')
        driver.get_screenshot_as_file(driver.session_id + '.png')
    finally:
        driver.quit()