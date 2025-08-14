<h2> Пример тестирования главной страницы <a target="_blank" href="https://promote.budget.gov.ru/">"Портала предоставления мер финансовой государственной поддержки"</a></h2>

<h3> Список UI проверок:</h3>

### Проверки, реализованные в автоматизированных тестах
- [x] Xедер
- Проверка отображения логотипа
- Проверка кликабельности кнопки "Навигатор"
- Проверка кликабельности кнопки "Техническая поддержка"
- Проверка кликабельности кнопки "Новости"
- Проверка кликабельности кнопки "Войти"
- [x] Виджеты подбора
- Проверка работы виджета "Подберите по ОГРН"
- Проверка работы виджета "Пройдите опрос"
- Проверка работы виджета "Подберите вручную"
- Подбор субсидийных отборов
- Подбор отборов социального заказа

----
### Проект реализован с использованием:
<div align="center">
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/python-original-wordmark.svg" 
    title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/pytest-original-wordmark.svg" 
    title="Pytest" alt="Pytest" width="45" height="45"/>&nbsp; 
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/selenium-original1.svg" 
    title="Selenium" alt="Selenium" width="40" height="40"/>&nbsp;  
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/selene.png" 
    title="Selene" alt="Selene" width="50" height="50"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/selenoid1.png" 
    title="Selenoid" alt="Selenoid" width="40" height="40"/>&nbsp; 
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/pycharm-original.svg" 
    title="PyCharm" alt="PyCharm" width="40" height="40"/>&nbsp;    
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/Allure.svg" 
    title="Allure Report" alt="Allure Report" width="40" height="40"/>&nbsp;
</div> 

----
### Локальный запуск

1. Склонировать репозиторий
2. Установить зависимости командой `pip install -r requirements.txt`
3. Открыть проект в PyCharm, установить интерпретатор
4. Запустить тесты в командной строке:
```bash
pytest -v
```
#### Пример прохождения тестов в терминале
![terminal](/resources/terminal.png)


----
### Allure отчет

#### Формирование отчета:
>-  ввести в командной строке `allure serve allure-results`


#### Пример сформированного отчета о прохождении тестов
![allure_owerview](/resources/allure_owerview.png)
![allure_suites](/resources/allure_suites.png)
![allure_graf](/resources/allure_graf.png)




----

### Пример видео прохождения автотеста
<p align="center">
    <img title="Video" src="/resources/video.gif">
</p>