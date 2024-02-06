import logging
import requests

def get_login():
    path = "https://test-stand.gb.ru/gateway/login"
    post = requests.post(url=path, data={'username': 'Monica Kunde V ', 'password': 'add9b80be1'})
    if post.status_code == 200:
            return post.json()['token']


def get_post(token):
   path =  "https://test-stand.gb.ru/api/posts"
   get  =  requests.get(url=path, params={"owner": "notMe"}, headers={"X-Auth-Token": token})
   if get.status_code == 200:
       return get.json()

def test_get_post(self, setup_api_with_auth):
        logging.info("Running test_get_post")
        response = setup_api_with_auth.get_post(1)
        assert response.status_code == 200

def test_create_post(self, setup_api_with_auth):
        logging.info("Running test_create_post")
        response = setup_api_with_auth.create_post("New post", "Hello world!")
        assert response.status_code == 201

def test_delete_post(self, setup_api_with_auth):
        logging.info("Running test_delete_post")
        response = setup_api_with_auth.delete_post(1)
        assert response.status_code == 204


if __name__ == '__main__':
    token = (get_login)
    print(get_post(token))