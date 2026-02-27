from playwright.sync_api import Locator
from pages.base_page import BasePage

class SearchResultsPage(BasePage):

    #Locators
    @property
    def results_title(self) -> Locator:
        return self.page. get_by_text('Результаты поиска')



    #Actions