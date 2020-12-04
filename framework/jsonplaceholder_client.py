import allure
import requests as r
from config import JSONPLACEHOLDER_HOST


class Client:

    def __init__(self):
        self.url = JSONPLACEHOLDER_HOST

    def _get(self, path: str):
        return r.get(url=self.url + path)

    def _post(self, path: str, data: dict):
        return r.post(url=self.url + path, data=data)

    def _delete(self, path: str):
        return r.delete(url=self.url + path)

    @allure.step
    def get_all_posts(self):
        return self._get(path=f'/posts')

    @allure.step
    def get_post_by_id(self, post_id: int):
        return self._get(path=f'/posts/{post_id}')

    @allure.step
    def get_album_by_user(self, user_id: int):
        return self._get(path=f'/albums?userId={user_id}')

    @allure.step
    def add_todo(self, data: dict):
        return self._post(path=f'/todos', data=data)

    @allure.step
    def delete_photo_by_id(self, photo_id: int):
        return self._delete(path=f'/photos/{photo_id}')
