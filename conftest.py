import pytest

import selene
from functools import lru_cache

from src import driver
from config import config


@pytest.fixture(scope="session" if config.test_run.ONE_SESSION else "function")
def selene_browser():
    selene_browsers = []

    def create(browser_name=None, version=None) -> selene.Browser:
        if browser_name is None:
            browser_name = "chrome"
        if version is None:
            version = "80.0"

        browser_config = selene.Config(
            driver=driver.create(browser_name=browser_name, version=version),
            timeout=30,
            hook_wait_failure=None,
            base_url="",
            set_value_by_js=False,
            type_by_js=False,
            window_width=None,
            window_height=None,
        )

        selene_browser = selene.Browser(config=browser_config)
        selene_browsers.append(selene_browser)
        return selene_browser

    yield lru_cache()(create) if config.test_run.ONE_SESSION else create

    for _selene_browser in selene_browsers:
        _selene_browser.quit()
