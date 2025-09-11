# qa_guru_lesson_17
rest api autotests

```python
(.venv) PS C:\Projects\PyCharm\qa_guru_lesson_17> pytest
======================================================================================================= test session starts =======================================================================================================
platform win32 -- Python 3.12.5, pytest-8.3.4, pluggy-1.6.0 -- C:\Projects\PyCharm\qa_guru_lesson_17\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Projects\PyCharm\qa_guru_lesson_17
configfile: pytest.ini
plugins: allure-pytest-2.15.0
collected 1 item / 4 errors                                                                                                                                                                                                        

============================================================================================================= ERRORS ============================================================================================================== 
___________________________________________________________________________ ERROR collecting tests/get_user_by_id/test_reqres_method_get_user_by_id.py ____________________________________________________________________________ 
ImportError while importing test module 'C:\Projects\PyCharm\qa_guru_lesson_17\tests\get_user_by_id\test_reqres_method_get_user_by_id.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\Alove\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests\get_user_by_id\test_reqres_method_get_user_by_id.py:8: in <module>
    from utils.path_helpers import get_schema_path
E   ModuleNotFoundError: No module named 'utils'
________________________________________________________________________________ ERROR collecting tests/get_users/test_reqres_method_get_users.py _________________________________________________________________________________ 
ImportError while importing test module 'C:\Projects\PyCharm\qa_guru_lesson_17\tests\get_users\test_reqres_method_get_users.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\Alove\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests\get_users\test_reqres_method_get_users.py:7: in <module>
    from utils.path_helpers import get_schema_path
E   ModuleNotFoundError: No module named 'utils'
______________________________________________________________________ ERROR collecting tests/post_clerk_link_pro/test_reqres_method_post_clerk_link_pro.py _______________________________________________________________________ 
ImportError while importing test module 'C:\Projects\PyCharm\qa_guru_lesson_17\tests\post_clerk_link_pro\test_reqres_method_post_clerk_link_pro.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\Alove\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests\post_clerk_link_pro\test_reqres_method_post_clerk_link_pro.py:9: in <module>
    from utils.path_helpers import get_schema_path
E   ModuleNotFoundError: No module named 'utils'
___________________________________________________________________________ ERROR collecting tests/put_user_by_id/test_reqres_method_put_user_by_id.py ____________________________________________________________________________ 
ImportError while importing test module 'C:\Projects\PyCharm\qa_guru_lesson_17\tests\put_user_by_id\test_reqres_method_put_user_by_id.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\Alove\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests\put_user_by_id\test_reqres_method_put_user_by_id.py:9: in <module>
    from utils.path_helpers import get_schema_path
E   ModuleNotFoundError: No module named 'utils'
===================================================================================================== short test summary info ===================================================================================================== 
ERROR tests/get_user_by_id/test_reqres_method_get_user_by_id.py
ERROR tests/get_users/test_reqres_method_get_users.py
ERROR tests/post_clerk_link_pro/test_reqres_method_post_clerk_link_pro.py
ERROR tests/put_user_by_id/test_reqres_method_put_user_by_id.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 4 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
======================================================================================================== 4 errors in 0.42s ======================================================================================================== 
(.venv) PS C:\Projects\PyCharm\qa_guru_lesson_17> pip install -r requirements.txt         
Collecting pytest==8.4.2 (from -r requirements.txt (line 1))
  Using cached pytest-8.4.2-py3-none-any.whl.metadata (7.7 kB)
Collecting requests==2.32.5 (from -r requirements.txt (line 2))
  Using cached requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Requirement already satisfied: jsonschema==4.25.1 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from -r requirements.txt (line 3)) (4.25.1)
Requirement already satisfied: allure-pytest==2.15.0 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from -r requirements.txt (line 4)) (2.15.0)
Requirement already satisfied: colorama>=0.4 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from pytest==8.4.2->-r requirements.txt (line 1)) (0.4.6)
Requirement already satisfied: iniconfig>=1 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from pytest==8.4.2->-r requirements.txt (line 1)) (2.1.0)
Requirement already satisfied: packaging>=20 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from pytest==8.4.2->-r requirements.txt (line 1)) (25.0)
Requirement already satisfied: pluggy<2,>=1.5 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from pytest==8.4.2->-r requirements.txt (line 1)) (1.6.0)
Collecting pygments>=2.7.2 (from pytest==8.4.2->-r requirements.txt (line 1))
  Using cached pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)
Requirement already satisfied: charset_normalizer<4,>=2 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from requests==2.32.5->-r requirements.txt (line 2)) (3.4.3)
Requirement already satisfied: idna<4,>=2.5 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from requests==2.32.5->-r requirements.txt (line 2)) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from requests==2.32.5->-r requirements.txt (line 2)) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from requests==2.32.5->-r requirements.txt (line 2)) (2025.8.3)
Requirement already satisfied: attrs>=22.2.0 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from jsonschema==4.25.1->-r requirements.txt (line 3)) (25.3.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from jsonschema==4.25.1->-r requirements.txt (line 3)) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from jsonschema==4.25.1->-r requirements.txt (line 3)) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from jsonschema==4.25.1->-r requirements.txt (line 3)) (0.27.1)
Requirement already satisfied: allure-python-commons==2.15.0 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from allure-pytest==2.15.0->-r requirements.txt (line 4)) (2.15.0)
Requirement already satisfied: typing-extensions>=4.4.0 in c:\projects\pycharm\qa_guru_lesson_17\.venv\lib\site-packages (from referencing>=0.28.4->jsonschema==4.25.1->-r requirements.txt (line 3)) (4.15.0)
Using cached pytest-8.4.2-py3-none-any.whl (365 kB)
Using cached requests-2.32.5-py3-none-any.whl (64 kB)
Using cached pygments-2.19.2-py3-none-any.whl (1.2 MB)
Installing collected packages: requests, pygments, pytest
  Attempting uninstall: requests
    Found existing installation: requests 2.32.3
    Uninstalling requests-2.32.3:
      Successfully uninstalled requests-2.32.3
  Attempting uninstall: pytest
    Found existing installation: pytest 8.3.4
    Uninstalling pytest-8.3.4:
      Successfully uninstalled pytest-8.3.4
Successfully installed pygments-2.19.2 pytest-8.4.2 requests-2.32.5                                                                                                                                                                 
(.venv) PS C:\Projects\PyCharm\qa_guru_lesson_17> pytest                         
======================================================================================================= test session starts =======================================================================================================
platform win32 -- Python 3.12.5, pytest-8.4.2, pluggy-1.6.0 -- C:\Projects\PyCharm\qa_guru_lesson_17\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Projects\PyCharm\qa_guru_lesson_17
configfile: pytest.ini
plugins: allure-pytest-2.15.0
collected 1 item / 4 errors                                                                                                                                                                                                        

============================================================================================================= ERRORS ============================================================================================================== 
___________________________________________________________________________ ERROR collecting tests/get_user_by_id/test_reqres_method_get_user_by_id.py ____________________________________________________________________________ 
ImportError while importing test module 'C:\Projects\PyCharm\qa_guru_lesson_17\tests\get_user_by_id\test_reqres_method_get_user_by_id.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\Alove\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests\get_user_by_id\test_reqres_method_get_user_by_id.py:8: in <module>
    from utils.path_helpers import get_schema_path
E   ModuleNotFoundError: No module named 'utils'
________________________________________________________________________________ ERROR collecting tests/get_users/test_reqres_method_get_users.py _________________________________________________________________________________ 
ImportError while importing test module 'C:\Projects\PyCharm\qa_guru_lesson_17\tests\get_users\test_reqres_method_get_users.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\Alove\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests\get_users\test_reqres_method_get_users.py:7: in <module>
    from utils.path_helpers import get_schema_path
E   ModuleNotFoundError: No module named 'utils'
______________________________________________________________________ ERROR collecting tests/post_clerk_link_pro/test_reqres_method_post_clerk_link_pro.py _______________________________________________________________________ 
ImportError while importing test module 'C:\Projects\PyCharm\qa_guru_lesson_17\tests\post_clerk_link_pro\test_reqres_method_post_clerk_link_pro.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\Alove\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests\post_clerk_link_pro\test_reqres_method_post_clerk_link_pro.py:9: in <module>
    from utils.path_helpers import get_schema_path
E   ModuleNotFoundError: No module named 'utils'
___________________________________________________________________________ ERROR collecting tests/put_user_by_id/test_reqres_method_put_user_by_id.py ____________________________________________________________________________ 
ImportError while importing test module 'C:\Projects\PyCharm\qa_guru_lesson_17\tests\put_user_by_id\test_reqres_method_put_user_by_id.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\Alove\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests\put_user_by_id\test_reqres_method_put_user_by_id.py:9: in <module>
    from utils.path_helpers import get_schema_path
E   ModuleNotFoundError: No module named 'utils'
===================================================================================================== short test summary info ===================================================================================================== 
ERROR tests/get_user_by_id/test_reqres_method_get_user_by_id.py
ERROR tests/get_users/test_reqres_method_get_users.py
ERROR tests/post_clerk_link_pro/test_reqres_method_post_clerk_link_pro.py
ERROR tests/put_user_by_id/test_reqres_method_put_user_by_id.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 4 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
======================================================================================================== 4 errors in 0.22s ======================================================================================================== 
(.venv) PS C:\Projects\PyCharm\qa_guru_lesson_17> pytest
======================================================================================================= test session starts =======================================================================================================
platform win32 -- Python 3.12.5, pytest-8.4.2, pluggy-1.6.0 -- C:\Projects\PyCharm\qa_guru_lesson_17\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Projects\PyCharm\qa_guru_lesson_17
configfile: pytest.ini
plugins: allure-pytest-2.15.0
collected 1 item / 4 errors                                                                                                                                                                                                        

============================================================================================================= ERRORS ============================================================================================================== 
___________________________________________________________________________ ERROR collecting tests/get_user_by_id/test_reqres_method_get_user_by_id.py ____________________________________________________________________________ 
ImportError while importing test module 'C:\Projects\PyCharm\qa_guru_lesson_17\tests\get_user_by_id\test_reqres_method_get_user_by_id.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\Alove\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests\get_user_by_id\test_reqres_method_get_user_by_id.py:8: in <module>
    from utils.path_helpers import get_schema_path
E   ModuleNotFoundError: No module named 'utils'
________________________________________________________________________________ ERROR collecting tests/get_users/test_reqres_method_get_users.py _________________________________________________________________________________ 
ImportError while importing test module 'C:\Projects\PyCharm\qa_guru_lesson_17\tests\get_users\test_reqres_method_get_users.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\Alove\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests\get_users\test_reqres_method_get_users.py:7: in <module>
    from utils.path_helpers import get_schema_path
E   ModuleNotFoundError: No module named 'utils'
______________________________________________________________________ ERROR collecting tests/post_clerk_link_pro/test_reqres_method_post_clerk_link_pro.py _______________________________________________________________________ 
ImportError while importing test module 'C:\Projects\PyCharm\qa_guru_lesson_17\tests\post_clerk_link_pro\test_reqres_method_post_clerk_link_pro.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\Alove\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests\post_clerk_link_pro\test_reqres_method_post_clerk_link_pro.py:9: in <module>
    from utils.path_helpers import get_schema_path
E   ModuleNotFoundError: No module named 'utils'
___________________________________________________________________________ ERROR collecting tests/put_user_by_id/test_reqres_method_put_user_by_id.py ____________________________________________________________________________ 
ImportError while importing test module 'C:\Projects\PyCharm\qa_guru_lesson_17\tests\put_user_by_id\test_reqres_method_put_user_by_id.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\Alove\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests\put_user_by_id\test_reqres_method_put_user_by_id.py:9: in <module>
    from utils.path_helpers import get_schema_path
E   ModuleNotFoundError: No module named 'utils'
===================================================================================================== short test summary info ===================================================================================================== 
ERROR tests/get_user_by_id/test_reqres_method_get_user_by_id.py
ERROR tests/get_users/test_reqres_method_get_users.py
ERROR tests/post_clerk_link_pro/test_reqres_method_post_clerk_link_pro.py
ERROR tests/put_user_by_id/test_reqres_method_put_user_by_id.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 4 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
======================================================================================================== 4 errors in 0.21s ======================================================================================================== 
(.venv) PS C:\Projects\PyCharm\qa_guru_lesson_17> 

```
