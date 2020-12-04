import allure
import pytest
from framework.check import check_get_all_posts_response, check_get_post_by_id_response
from framework.helper import prepare_single_data


@allure.suite('GET /posts')
class TestGetPosts:

    @allure.title('Positive. Get all posts')
    def test_get_all_posts(self, client):
        response = client.get_all_posts()
        check_get_all_posts_response(response)

    # негативный тест на получение конкретного поста (GET)
    @pytest.mark.parametrize('id', [prepare_single_data('id', positive=False) for x in range(1, 6)])
    @allure.title('Negative. Get post by id')
    def test_get_post_by_id_neg(self, client, id):
        response = client.get_post_by_id(id)
        check_get_post_by_id_response(response)
