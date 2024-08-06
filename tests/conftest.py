import pytest
from selene import browser


@pytest.fixture(scope='function', params=[(1920, 1080), (1280, 720), (430, 932)])
def setup_browser(request):
    width, height = request.param

    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.base_url = 'https://github.com'

    if width > 800:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()


@pytest.fixture(scope='function', params=[(430, 932), (390, 844)])
def setup_browser_mobile(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.base_url = 'https://github.com'

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(1920, 1080), (1280, 720)])
def setup_browser_desktop(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.base_url = 'https://github.com'

    yield

    browser.quit()
