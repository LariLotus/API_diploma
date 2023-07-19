# API_diploma
# Использованные инструменты
<p align="left">
<code><img width="5%" title="Python" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1024px-Python.svg.png"></code>
<code><img width="5%" title="Pycharm" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1200px-PyCharm_Icon.svg.png"></code>
<code><img width="5%" title="Pytest" src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg"></code>
<code><img width="5%" title="Requests" src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png"></code>
<code><img width="5%" title="Allure Report" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4"></code>
<code><img width="5%" title="Allure TestOps" src="https://marketplace-cdn.atlassian.com/files/92e2d8c3-2a30-46c0-bf21-2453a4a270d3?fileType=image&mode=full-fit"></code>
<code><img width="5%" title="GitHub" src="https://cdn-icons-png.flaticon.com/512/25/25231.png"></code>
<code><img width="5%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"></code>
</code>
</p>
## Описание проекта
Учебный проект реализации автотестирования **Rest Api**.<br/>
>В качестве объекта тестирования выбран сайт https://reqres.in/ с открытым api.<br/>

## Список проверок, реализованных в автотестах:
:sparkle: Проверка списка пользователей

:sparkle: Проверка создания нового пользователя

:sparkle: Проверка пользователя по заданному id 6

:sparkle: Проверка обновления id, name, job пользователя

:sparkle: Проверка удаления пользователя

:sparkle: Проверка ошибки авторизации пользователя

## Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/API_diploma/allure/">Ссылка на проект в Jenkins</a>

![This is an image](/resourses/jenkins.png)

Для запуска тестов выбрать пункт **"Собрать сейчас"**

## Отчеты о прохождении тестов доступны в Allure
![This is an image](/resourses/Allure_report.png)

![This is an image](/resourses/Allure_graphs.png)

![This is an image](/resourses/Allure_behaviors.png)

## Проект интегрирован с Allure TestOps

### Итоговые dashboard по результатам сборок
![This is an image](/resourses/AllureTestOps_dashboard.png)
![This is an image](/resourses/TestOps_testcases.png)


### Аналитическая dashboard с Features и Launches
![This is an image](/resourses/AllureTestOps_features.png)
![This is an image](/resourses/AllureTestOps_launchers.png)

## Интеграция с Jira
### Настроив через Allure TestOps интеграцию с Jira, в тикет можно пробросить результат прохождение тестов и список тест-кейсов из Allure
![This is an image](/resourses/jira.png)

## Интеграция с Telegram
### После прохождения тестов, в Telegram bot приходит сообщение с графиком и краткой информацией о тестах
![This is an image](/resourses/telegram1.png)









