import allure
import pytest
from framework.check import check_delete_photo_by_id_response
from framework.helper import prepare_single_data


@allure.suite('DELETE /photo')
class TestDeletePhoto:

    # позитивный тест на удаление фото (DELETE)
    @pytest.mark.parametrize('id', [prepare_single_data('id') for x in range(1, 6)])
    @allure.title('Positive. Delete photo by id')
    def test_delete_album_by_id(self, client, id):
        response = client.delete_photo_by_id(id)
        check_delete_photo_by_id_response(response)
