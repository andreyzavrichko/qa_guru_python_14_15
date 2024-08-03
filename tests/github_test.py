import pytest
from selene import browser, be


def test_sign_in(setup_browser):
    browser.open('/')
    browser.element("//a[contains(@class, 'HeaderMenu-link--sign-in')]").click()
    browser.element("//h1").should(be.visible)


def test_sign_in_desktop(setup_browser):
    if setup_browser == 'mobile':
        pytest.skip(reason='Разрешение экрана для мобильной версии, тест пропущен.')

    browser.open('/')
    browser.element("//a[contains(@class, 'HeaderMenu-link--sign-in')]").click()
    browser.element("//h1").should(be.visible)


def test_sign_in_mobile(setup_browser):
    if setup_browser == 'desktop':
        pytest.skip(reason='Разрешение экрана для десктопной версии, тест пропущен.')

    browser.open('/')
    browser.element('.Button-label').click()
    browser.element("//a[contains(@class, 'HeaderMenu-link HeaderMenu-button')]").click()
    browser.element("//h1").should(be.visible)


@pytest.mark.parametrize("setup_browser", [(1920, 1080), (430, 932)], indirect=True)
def test_sign_in_indirect(setup_browser):
    browser.open('/')
    if setup_browser == 'desktop':
        browser.element("//a[contains(@class, 'HeaderMenu-link--sign-in')]").click()
    else:
        browser.element('.Button-label').click()
        browser.element("//a[contains(@class, 'HeaderMenu-link HeaderMenu-button')]").click()

    browser.element("//h1").should(be.visible)


def test_github_desktop(setup_browser_desktop):
    browser.open('/')
    browser.element("//a[contains(@class, 'HeaderMenu-link--sign-in')]").click()
    browser.element("//h1").should(be.visible)


def test_github_mobile2(setup_browser_mobile):
    browser.open('/')
    browser.element('.Button-label').click()
    browser.element("//a[contains(@class, 'HeaderMenu-link HeaderMenu-button')]").click()
    browser.element("//h1").should(be.visible)
