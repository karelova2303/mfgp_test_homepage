import allure

from mfgp_test_homepage.app import app


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Xедер')
class TestHeader:

    @allure.title('Отображение логотипа')
    def test_visible_logo(self, browser_manager, attach_with_test):
        app.page_header.should_visible_logo('Портал предоставления мер финансовой')

    @allure.title('Проверка кликабельности кнопки "Навигатор"')
    def test_click_button_navigation(self, browser_manager, attach_with_test):
        app.page_header.should_be_clickable_btn_navigation('Навигатор')

    @allure.title('Проверка кликабельности кнопки "Техническая поддержка"')
    def test_click_button_support(self, browser_manager, attach_with_test):
        app.page_header.should_be_clickable_btn_support('Техническая поддержка')

    @allure.title('Проверка кликабельности кнопки "Новости"')
    def test_click_button_news(self, browser_manager, attach_with_test):
        app.page_header.should_be_clickable_btn_news('Новости')

    @allure.title('Проверка кликабельности кнопки "Войти"')
    def test_click_button_login(self, browser_manager, attach_with_test):
        app.page_header.should_be_clickable_btn_login('Войти')


@allure.tag('Web', 'Prod')
@allure.label('owner', 'Karelova Ekaterina')
@allure.suite('Виджеты подбора')
class TestSelectionOnTheMainPage:

    @allure.title('Проверка работы виджета "Подберите по ОГРН"')
    def test_click_widget_select_by_ogrn(self, browser_manager, attach_with_test):
        app.page_content.click_widget_select_by_ogrn('Подбор по ОГРН')

    @allure.title('Проверка работы виджета "Пройдите опрос"')
    def test_click_widget_take_the_quiz(self, browser_manager, attach_with_test):
        app.page_content.click_widget_take_the_quiz('Подбор мер поддержки')

    @allure.title('Проверка работы виджета "Подберите вручную"')
    def test_click_widget_manual_selection(self, browser_manager, attach_with_test):
        app.page_content.click_widget_manual_selection('Все фильтры')

    @allure.title('Подбор субсидийных отборов')
    def test_search_subsidy_selection(self, browser_manager, attach_with_test):
        app.page_content.search_subsidy_selection('Отборы по субсидиям')

    @allure.title('Подбор отборов социального заказа')
    def test_search_social_order_selection(self, browser_manager, attach_with_test):
        app.page_content.search_social_order_selection('Отборы по социальному заказу')
