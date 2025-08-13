import allure
from selene import browser, be, have, command


# class OpenPage:
#
#     def open_homepage(self):
#         with allure.step('Открываем Главную страницу'):
#             browser.open('/')

class HeaderPage:
    def __init__(self):
        self.search_logo = browser.element('.header-logo')
        self.search_logo_text = browser.element('.header-logo__text')

        self.header_menu = browser.element('.header')
        self.btn_navigation = self.header_menu.element('[href="/public/minfin/activity"]')
        self.navigator_title = browser.element('.navigator__title')

        self.btn_support = self.header_menu.element('[href="/support-center/main"]')
        self.support_title = browser.element('.support-page__title')

        self.btn_news = self.header_menu.element('[href="/public/news/news-list"]')
        self.news_title = browser.element('.news-list__title')

        self.btn_login = self.header_menu.element('[type="button"]')
        self.authorization_btn = browser.element('.authorization-btn')

    def open_homepage(self):
        with allure.step('Открываем Главную страницу'):
            browser.open('/')

    def should_visible_logo(self, value):
        self.open_homepage()
        with allure.step('Проверяем отображение логотипа'):
            self.search_logo.should(be.visible)
            self.search_logo_text.should(have.text(value))

    def should_be_clickable_btn_navigation(self, value):
        self.open_homepage()
        with allure.step(f'Кликаем кнопку "{value}"'):
            self.btn_navigation.click()
            self.navigator_title.should(have.exact_text(value))

    def should_be_clickable_btn_support(self, value):
        self.open_homepage()
        with allure.step(f'Кликаем кнопку "{value}"'):
            self.btn_support.click()
            self.support_title.should(have.text(value))

    def should_be_clickable_btn_news(self, value):
        self.open_homepage()
        with allure.step(f'Кликаем кнопку "{value}"'):
            self.btn_news.click()
            self.news_title.should(have.exact_text(value))

    def should_be_clickable_btn_login(self, value):
        self.open_homepage()
        with allure.step(f'Кликаем кнопку "{value}"'):
            self.btn_login.click()
            self.authorization_btn.should(be.visible)


class PageContent():
    def __init__(self):
        self.widgets_title = browser.element('.main-auto-selection')
        self.widgets = browser.all('.main-auto-selection__item')

        self.modal_widget = browser.element('.minfin-selection-modal__title')
        self.modal_filter = browser.element('.navigator-filter__title')

        self.main_categories = browser.all('.main-categories-item')
        self.btn_find_subsidy = self.main_categories.first.element('.mrx-btn')
        self.btn_find_social_order = self.main_categories.second.element('.mrx-btn')
        self.navigator_type_title = browser.element('.navigator-type__title')

    def open_homepage(self):
        with allure.step('Открываем Главную страницу'):
            browser.open('/')

    def click_widget_select_by_ogrn(self, value):
        self.open_homepage()
        with allure.step(f'Кликаем виджет "{value}"'):
            self.widgets.first.perform(command.js.scroll_into_view).click()
        with allure.step(f'Отображается модалка "{value}"'):
            self.modal_widget.should(have.exact_text(value))

    def click_widget_take_the_quiz(self, value):
        self.open_homepage()
        with allure.step(f'Кликаем виджет "{value}"'):
            self.widgets.second.perform(command.js.scroll_into_view).click()
        with allure.step(f'Отображается модалка "{value}"'):
            self.modal_widget.should(have.exact_text(value))

    def click_widget_manual_selection(self, value):
        self.open_homepage()
        with allure.step(f'Кликаем виджет "{value}"'):
            self.widgets[2].perform(command.js.scroll_into_view).click()
        with allure.step(f'Отображается модалка "{value}"'):
            self.modal_filter.with_(timeout=25).should(have.exact_text(value))

    def search_subsidy_selection(self, value):
        self.open_homepage()
        with allure.step(f'Кликаем кнопку "Найти"'):
            self.btn_find_subsidy.perform(command.js.scroll_into_view).click()
        with allure.step(f'Проверяем отображение подборки "{value}"'):
            self.navigator_type_title.should(have.exact_text(value))

    def search_social_order_selection(self, value):
        self.open_homepage()
        with allure.step(f'Кликаем кнопку "Найти"'):
            self.btn_find_social_order.perform(command.js.scroll_into_view).click()
        with allure.step(f'Проверяем отображение подборки "{value}"'):
            self.navigator_type_title.should(have.exact_text(value))
