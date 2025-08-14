import allure_commons
import pytest

from selene import browser, support

from utils import attach


@pytest.fixture(scope='session', autouse=True)
def browser_manager():
    browser.config.base_url = 'https://promote.budget.gov.ru'
    browser.driver.maximize_window()

    yield

    browser.quit()

@pytest.fixture(scope='function')
def attach_with_test():
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)