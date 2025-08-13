from mfgp_test_homepage.pages.page_mainpage import HeaderPage, PageContent


class ApplicationManager:
    def __init__(self):
        self.page_header = HeaderPage()
        self.page_content = PageContent()

app = ApplicationManager()