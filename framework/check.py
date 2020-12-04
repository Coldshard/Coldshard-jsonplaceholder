import allure
from hamcrest import assert_that, equal_to, empty, is_in
from requests import codes
from config import ResourceLimits as rl


def _response_code_general_check(response, expected_code=codes.ok):
    code = response.status_code
    assert_that(code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {code}. Url: {response.url}')


def _response_length_general_check(response, expected_value1=1, expected_value2=1, comparison='equal'):
    length = len(response.json())
    if comparison == 'equal':
        assert_that(length, equal_to(expected_value1),
                    f'Expected length: {expected_value1}. Actual length: {length}. Url: {response.url}')
    elif comparison == 'in':
        assert_that(length, is_in(range(expected_value1, expected_value2+1)),
                    f'Expected length between {expected_value1} and {expected_value2}. \
                      Actual length: {length}. Url: {response.url}')
    elif comparison == 'empty':
        assert_that(response.json(), empty(),
                    f'Expected to be empty. Actual length: {length}. Url: {response.url}')


def _response_type_general_check(response, expected_type='application/json; charset=utf-8'):
    type = response.headers['Content-Type']
    assert_that(type, equal_to(expected_type),
                f'Expected content type: {expected_type}. Actual type: {type}. Url: {response.url}')


def _base_check_set(response, method='get', code=codes.ok, min_len=1, max_len=1,
                    comp='eq', content='application/json; charset=utf-8', negative=False):
    _response_code_general_check(response, code)
    _response_type_general_check(response, content)
    if method == 'get':
        _response_length_general_check(response, min_len, max_len, comp)


@allure.step
def check_get_all_posts_response(response):
    _base_check_set(response, max_len=rl.limits['posts'])


@allure.step
def check_get_post_by_id_response(response):
    _base_check_set(response)


@allure.step
def check_get_post_by_id_response_neg(response):
    _base_check_set(response, comp='empty')


@allure.step
def check_get_album_by_user_response(response):
    _base_check_set(response, max_len=rl.limits['albums'])


@allure.step
def check_get_album_by_user_response_neg(response):
    _base_check_set(response, comp='empty')


@allure.step
def check_add_todo_response(response):
    _base_check_set(response, method='post', code=201)


@allure.step
def check_delete_photo_by_id_response(response):
    _base_check_set(response, method='delete')
