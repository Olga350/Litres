from playwright.sync_api import Page, expect

def test_titles(page: Page):
    expect(page).to_have_title('Литрес – сервис электронных и аудиокниг, скачать в fb2 и mp3, читать и слушать онлайн на Litres')
    
def test_audiobooks_title(page:Page):
    page.locator('xpath= //*[@id="lowerMenuWrap"]/nav/div/a[7]').click()
    expect(page).to_have_title('Аудиокниги – слушать онлайн или скачать в mp3 на Литрес')
