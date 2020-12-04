import allure
import pytest
from framework.check import check_add_todo_response
from framework.helper import prepare_mass_data


@allure.suite('POST /todos')
class TestAddTodos:

    # позитивный тест на добавление нового todo (POST)
    @pytest.mark.parametrize('data', [prepare_mass_data('todo') for x in range(1, 6)])
    @allure.title('Positive. Add post')
    def test_add_todo(self, client, data):
        response = client.add_todo(data)
        check_add_todo_response(response)
