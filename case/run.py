import pytest,time
from case.driver import init_driver

if __name__ == '__main__':
    driver = init_driver()
    time.sleep(5)
    pytest.main(["test_login.py"])


