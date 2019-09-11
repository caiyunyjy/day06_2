from base.bage_login import Bage
from page.page_login import PageLogin


class PageIn:
    def get_page_login(self):
        return PageLogin(Bage)