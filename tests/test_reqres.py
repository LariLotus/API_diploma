import allure
from allure_commons.types import Severity
import schemas.schemas_reqres
from api.reqres import get_list_users, post_create_users, update_user, \
    get_user, delete_user, post_register_user
from pytest_voluptuous import S
from models import data_reqres
from models.data_reqres import base_url


@allure.tag('api')
@allure.label('owner', 'Larisa')
@allure.description('Список пользователей')
@allure.feature('Проверка списка пользователей')
@allure.link(f'{base_url}/api/users')
def test_list_users():
    with allure.step(f' Создаем GET запрос c параметром page={data_reqres.page}'):
        response = get_list_users(params={"page": data_reqres.page})
    with allure.step('Проверка статус-кода и списка пользователей'):
        assert response.status_code == 200
        assert response.json()['page'] == data_reqres.page
        assert len(response.json()['data']) != 0


@allure.tag('api')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Larisa')
@allure.description('Создание пользователя')
@allure.feature('Проверка создания пользователя при вводе валидных данных')
@allure.link(f'{base_url}/api/users')
def test_create_user(name=data_reqres.create_name, job=data_reqres.create_job):
    with allure.step(f'POST запрос c валидными данными в теле запроса'):
        response = post_create_users(name, job)
    with allure.step('Проверка успешного создания и соответствия введенных данных'):
        assert response.status_code == 201
        assert response.json()['name'] == name
        assert response.json()['job'] == job
    with allure.step('Проверка соответствия ответа схеме'):
        assert response.json() == S(schemas.schemas_reqres.create_user_schema)


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Larisa')
@allure.description('Список пользователей')
@allure.feature(f'Проверка пользователя по заданному id {data_reqres.id_user}')
@allure.link(f'{base_url}/api/users/{data_reqres.id_user}')
def test_get_user(id_user=data_reqres.id_user):
    with allure.step(f'GET запрос c id пользователя'):
        response = get_user(id_user)
    with allure.step(f'Проверка данных пользователя с id {data_reqres.id_user}'):
        assert response.status_code == 200
        assert response.json()['data']['id'] == 6
        assert response.json()['data']['email'] == 'tracey.ramos@reqres.in'
        assert response.json()['data']['first_name'] == 'Tracey'
        assert response.json()['data']['last_name'] == 'Ramos'
    with allure.step('Проверка соответствия ответа схеме'):
        assert response.json() == S(schemas.schemas_reqres.get_user_schema)


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Larisa')
@allure.description('Обновление пользователей')
@allure.feature('Проверка обновления id, name, job пользователя')
@allure.link(f'{base_url}/api/users/{data_reqres.id_user_update}')
def test_update_user(id_user=data_reqres.id_user_update, name=data_reqres.name_update,
                     job=data_reqres.job_update):
    with allure.step('POST запрос с валидными данными'):
        response = update_user(id_user, name, job)
    with allure.step('Проверка успешного обновления пользователя'):
        assert response.status_code == 200
        assert response.json()['name'] == name
        assert response.json()['job'] == job
    with allure.step('Проверка соответствия ответа схеме'):
        assert response.json() == S(schemas.schemas_reqres.update_user_schema)


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Larisa')
@allure.description('Удаление пользователей')
@allure.feature('Проверка удаления пользователя')
@allure.link(f'{base_url}/api/users/{data_reqres.user_id_delete}')
def test_delete_user(id_user=data_reqres.user_id_delete):
    with allure.step(f'Отправка запроса DELETE с id {data_reqres.user_id_delete}'):
        response = delete_user(id_user)
    with allure.step('Проверка соответствия статус-коду'):
        assert response.status_code == 204


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Larisa')
@allure.description('Авторизация пользователя')
@allure.feature('Проверка ошибки авторизации пользователя')
@allure.link(f'{base_url}/api/register')
def test_fail_register_user():
    with allure.step('POST запрос без обязательного параметра password'):
        response = post_register_user(email='test@test123.test')
    with allure.step('Проверка статус-кода и ошибки в ответе'):
        assert response.status_code == 400
        assert response.json()['error'] == 'Missing password'
    with allure.step('Проверка соответствия ответа схеме'):
        assert response.json() == S(schemas.schemas_reqres.post_unsuccesses_register_user)
