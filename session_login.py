import requests
import unittest


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.session.close()

    def test_login1(self):
        response = self.session.get('http://127.0.0.1/index.php?m=Home&c=User&a=verify')
        self.assertEqual('image/png', response.headers.get('Content-Type'))
        response = self.session.post('http://127.0.0.1/index.php?m=Home&c=User&a=do_login&t=0.0776510818324554',
                                     data={"username": "18888888888", "password": "666666", "verify_code": "8888"})
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json().get('status'))
        self.assertIn('登陆成功', response.json().get('msg'))

    def test_login2(self):
        response = self.session.get('http://127.0.0.1/index.php?m=Home&c=User&a=verify')
        self.assertEqual('image/png', response.headers.get('Content-Type'))
        response = self.session.post('http://127.0.0.1/index.php?m=Home&c=User&a=do_login&t=0.0776510818324554',
                                     data={"username": "10088888888", "password": "666666", "verify_code": "8888"})
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, response.json().get('status'))
        self.assertIn('不存在', response.json().get('msg'))
