import pytest
class Test_login2(object):
    def setup_class(cls):
        print('第三')
    def teardown_class(cls):
        print('第四')
    def test_01(self):
        print(2)
if __name__ == '__main__':
    pytest.main(["test_02.py"])