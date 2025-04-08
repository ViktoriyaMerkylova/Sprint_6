# Sprint 6: UI-тестирование с помощью Page Object Model и Allure сервиса «Яндекс.Самокат»


# О проекте:

Практикум по Page Object, направленный на тестирование веб-приложения «Яндекс.Самокат».



# Запуск тестов

1. Основа для написания автотестов - pytest, selenium
    
2. Установить зависимости:
    
    
    pip install pytest
    pip install selenium

3. Установить зависимости:

     > pip install -r requirements.txt


4. Команда для запуска: 
    
    
    pytest -v tests

5. Просмотреть отчет:
 
    Запуск тестов с генерацией от allure 
    pytest --alluredir=allure-results
    
    Просмотр тестов в браузере
    allure serve allure-results

