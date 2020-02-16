from selenium import webdriver

from config import config

host = "http://test:test-password@localhost:4445/wd/hub" if config.test_run.GGR else "http://localhost:4444/wd/hub"


def create(browser_name, version):
    capabilities = {
        "browserName": browser_name,
        "version": version,
        "platform": "LINUX",
        "enableVNC": False,
        "enableVideo": False,
        "enableLog": False,
        "screenResolution": "1024x768x24",
        "sessionTimeout": "30s",
    }
    _driver = webdriver.Remote(command_executor=host, desired_capabilities=capabilities)

    return _driver
