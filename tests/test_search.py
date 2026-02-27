
from playwright.sync_api import Page, expect


def test_main_actions(page, home):
    #page.get_by_test_id('search__input').fill('python')
    #page.keyboard.press('Enter')
    query = "python"
    home.search(query)
    expect(page.get_by_text('Результаты поиска «python»'))
    page.locator('xpath=//*[@aria-description = "Книги, которые можно читать без ограничений с активной Литрес: Подпиской"]').click()
    #page.screenshot(path='../screenshot/toggle.png')
    page.check('label[for="languages-ru"]')


def test_wait(page, home):
    #page.get_by_placeholder('Искать на Литрес').fill('Самоучитель Python')
    #page.get_by_test_id('search__button').click()
    query = "Самоучитель Python"
    home.search(query)
    expect(page.get_by_text('Результаты поиска «Самоучитель Python»')).to_be_visible
    expect(page).to_have_title('Результаты поиска по книгам: «Самоучитель Python»')
    books = page.get_by_test_id('art__wrapper')
    expect(books).to_have_count(24, timeout=10000)

    
    page.pause

