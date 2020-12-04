import allure
import pytest
from framework.check import check_get_album_by_user_response
from framework.helper import prepare_single_data


@allure.suite('GET /albums')
class TestGetAlbums:

    # негативный тест на получение альбомов по user_id (GET)
    @pytest.mark.parametrize('user_id', [prepare_single_data('userId', positive=False) for x in range(1, 6)])
    @allure.title('Negative. Get albums by user')
    def test_get_album_by_user_neg(self, client, user_id):
        response = client.get_album_by_user(user_id)
        check_get_album_by_user_response(response)
