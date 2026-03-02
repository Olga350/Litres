
from playwright.sync_api import Page, expect


def test_main_actions(page, home, results):
    #page.get_by_test_id('search__input').fill('python')
    #page.keyboard.press('Enter')
    query = "python"
    home.search(query)
    #expect(page.get_by_text('Результаты поиска «python»'))
    #page.locator('xpath=//*[@aria-description = "Книги, которые можно читать без ограничений с активной Литрес: Подпиской"]').click()
    #page.screenshot(path='../screenshot/toggle.png')
    #page.check('label[for="languages-ru"]')
    results.apply_russian_filter()
    expect(results.russian_chip).to_be_visible


def test_wait(page, home, results):
    #page.get_by_placeholder('Искать на Литрес').fill('Самоучитель Python')
    #page.get_by_test_id('search__button').click()
    #books = page.get_by_test_id('art__wrapper')

    query = "Самоучитель Python"
    home.search(query)
    expect(results.results_title).to_contain_text(query)
   
    expect(results.books).to_have_count(24, timeout=10000)



