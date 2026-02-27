from playwright.sync_api import Page, expect


def test_locators(page: Page):
    page.get_by_role('link', name = 'Подписка за 0 ₽').click()
    expect(page).to_have_title('Литрес Подписка – множество аудиокниг и подкастов')

def test_placeholder(page: Page):
    page.get_by_placeholder('Искать на Литрес').fill('татьяна устинова')
    page.keyboard.press('Enter')
    expect(page.get_by_text('Результаты поиска «татьяна устинова»')).to_be_visible

def test_datatestid(page: Page):
    page.get_by_test_id('header-catalog-button').click()
    expect(page.get_by_text('Легкое чтение')).to_be_visible

#def test_alt(page: Page):
    page.goto('https://www.litres.ru/audiobooks/')
    page.get_by_role('button', name = 'Принять').click()
    page.get_by_alt_text('Логотип Литрес').click()
    expect(page.get_by_title('Литрес – сервис электронных и аудиокниг, скачать в fb2 и mp3, читать и слушать онлайн на Litres'))
