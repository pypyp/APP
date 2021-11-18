import pytest
def setup_module():
    print ("setup_module():在模块最之前执行\n")

def teardown_module():
    print ("teardown_module：在模块之后执行")
class Test_login1(object):
    def setup_class(self):
        print('第一')
    def teardown_class(self):
        print('第二')
    def test_01(self,get_token):
        print(get_token)
        print(1)
if __name__ == '__main__':
    pytest.main(["test_01.py"])
