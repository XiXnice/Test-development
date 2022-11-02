import unittest
from parameterized import parameterized
from api_yd import put_resources, TOKEN_YD, url_yd

FIXTURES = [
    (TOKEN_YD, url_yd, 'image', 200, 'image'),
    (TOKEN_YD, url_yd, 'foto', 200, 'foto'),
    (TOKEN_YD, url_yd, 'qwe', 200, 'qwe'),
    (TOKEN_YD, url_yd, 'asd', 200, 'asd'),
    (TOKEN_YD, url_yd, 'zxc', 200, 'zxc')
]

class TestFuctions(unittest.TestCase):
    @parameterized.expand(FIXTURES)
    def test_put_resources(self, a, b, c, exp_status_result, exp_folder_result):
        status_result, folder_result = put_resources(a, b, c)
        self.assertEquals((exp_status_result, exp_folder_result), (status_result, folder_result))