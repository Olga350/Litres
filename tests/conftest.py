import pytest
from playwright.sync_api import Page

@pytest.fixture(autouse=True)
def open_litres(page: Page):
    page.goto('https://www.litres.ru/')
    #page.get_by_role('button', name = 'Принять').click()