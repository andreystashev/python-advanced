import unittest
from module_04_flask.hw.hw_1_2 import app


class TestRegisterForm(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.data = {
            'email': 'mail@mail.ru',
            'phone': '8005553535',
            'name': 'Joe',
            'address': 'Kyprus',
            'index': '100000',
            'comment': 'hello world'
        }

    def test_valid_all_data(self):
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_email_format(self):
        self.data['email'] = 'mail.ru'
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_email(self):
        self.data['email'] = ''
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_phone_min(self):
        self.data['phone'] = '0'
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_phone_max(self):
        self.data['phone'] = '100000000000'
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_phone_type(self):
        self.data['phone'] = 'hello'
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_phone(self):
        self.data['phone'] = ''
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_name(self):
        self.data['name'] = ''
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_address(self):
        self.data['address'] = ''
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_index_type(self):
        self.data['index'] = 'hello'
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_index(self):
        self.data['index'] = ''
        response = self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 400)
