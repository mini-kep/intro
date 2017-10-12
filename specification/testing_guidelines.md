Testing guidelines
==================

These guidelines cover unit tests (being) developped at various parts of ```mini-kep``` project.

We do not have functional (eg selenium) or load tests, which may have slightly different logic 
or requirements in some aspects. 

Introduction
------------

Testing is known to be even harder than writing original code. 

When testing one must think of: 
- how the code under test is supposed to run well 
- how the code under test may run with error
- how to expose behaviours above in test setup and checks?
- how to write test in a clean and understandable fashion? how to name tests?
- how to effectively mock functions to avoid third-party access and simulate real-time inputs 
- what conditions / arguments are most probable for the code under test?
- what happens in program outside code under test?

Tests should :
- show where are bugs in the code
- show where original code needs enhancements to cover possible edge situations

Checklist
----------

Best tests:
1. run quick and often
2. use a continious integration like Travis CI and use coverage metrics like codecov 
3. cover at least all public methods/functions
4. have long names with context and expected result (except very short tests)
5. are as simple and readable as they can get 
6. one test tests one thing and has one assert per test
7. have clear separation of setup, call of code under test and check 
8. make good use of parametrisation, fixtures, dependency injection, mocks and monkey-patching
9. concentrate around practical, not fantasy situations  
10. include just a few integration, end-to-end tests
11. fail early and close to where problem is

Learning
--------
Basic testing in python :
- <http://docs.python-guide.org/en/latest/writing/tests/>

Takeaways from <https://pylonsproject.org/community-unit-testing-guidelines.html>:
- tests should be as simple as possible
- tests should be isolated
- each test method should test Just One Thing

References about:
- testing is not the best technique to ensure code quality

Tests samples for function fetch(url)
-----------------------------------
Original function fetch(url) is simple method which takes one input argument with type ```str```. Input argument reflect URL which is accessed via ```requests.get``` method provided by ```requests``` package. ```requests.get``` method returns ```requests``` object which has available ```.text``` attribute to returns text from acceessed URL. This is stored in ```content``` variable. Function throws expections when ```Error``` or ```Error in parameters``` string is present in fetched content, else it returns text content of accessed URL.

```
def fetch(url):
    """Fetch content from *url* from internet."""
    content = requests.get(url).text
    if "Error" in content:
        raise ValueError(f"Cannot read from URL <{url}>")
    if 'Error in parameters' in content:
        raise Exception(f'Error in parameters: {url}')
    return content
```
Tests for function fetch():
```
import pytest
import requests_mock
from parsers.getter.util import fetch

#fixtures
@pytest.fixture(scope='module')
def mocked_content():
    with requests_mock.mock() as mocked_content:
        yield mocked_content

@pytest.fixture
def setup_url():
    url = "http://www.testpage.com"
    yield url

class Test_fetch:

    def test_fetch_good_response(self, mocked_content, setup_url):
        mocked_content.get(setup_url, text="good response from url")
        assert fetch(setup_url) == 'good response from url'

    def test_fetch_with_non_readable_URL_raises_ValueError(self, mocked_content, setup_url):
        with pytest.raises(ValueError):
            mocked_content.get(setup_url, text="Error reponse")
            fetch(setup_url)

    def test_fetch_returns_Error_in_parameters_raises_Exception(self, mocked_content, setup_url):
        with pytest.raises(Exception):
            mocked_content.get(setup_url, text="Error in parameters")
            fetch(setup_url)
```
Tests naming convention
-----------------------
Tests have to be named properly to clearly tell
- which function is tested.
- what input is given
- what is the expected result or behaviour

Test naming convention for test with valid parameters:
```test_FUNCTION_NAME_with_valid_INPUT_ARGUMENTS()```

Test naming convention for tests with invalid parameters:
```test_FUNCTION_NAME_with_invalid_INPUT_ARGUMENTS_DOES_WHAT()```

Tests for function ```format_date()``` following above given tests naming conventions:
--------------------------------------------------------------------------------------

Function ```format_date(date_string: str, fmt)``` is accepting 2 positional input arguments, both as ```str``` type. First ```date_string``` argument reflects input date itself, second ```fmt``` argument tels function ```datetime.strptime``` which date format use to translate ```date_string``` into ```datetime type``` and then translate it again into ```str``` type with function ```strftime``` to return date with given date format. 

Usage:

```format_date('02.06.1993', fmt="%d.%m.%Y")```

Definition:

```
def format_date(date_string: str, fmt):
    return datetime.strptime(date_string, fmt).strftime("%Y-%m-%d")
```
Tests for above function:
```
class Test_format_date:
    def test_format_date_with_valid_date_string(self):
        assert format_date('2017-01-04T00:00:00', fmt='%Y-%m-%dT%H:%M:%S') == '2017-01-04'
        assert format_date('20170104', fmt="%Y%m%d") == '2017-01-04'

    def test_format_date_with_invalid_date_string_raises_ValueError(self):
        with pytest.raises(ValueError):
            format_date('bad_date_format', fmt='%Y-%m-%dT%H:%M:%S')
        with pytest.raises(ValueError):
            format_date('bad_date_format', fmt="%Y%m%d")

    def test_format_date_with_None_raises_TypeError(self):
        with pytest.raises(TypeError):
            format_date(None, fmt='%Y-%m-%dT%H:%M:%S')
        with pytest.raises(TypeError):
            format_date(None, fmt="%Y%m%d")
```


To cover 
--------
- testing in flask with db

Prior discussions
-----------------
- Flask testing: <https://github.com/mini-kep/frontend-app/issues/7>
- parsers testing: <https://github.com/mini-kep/parsers/issues/15>
- earlier on parsers testing: <https://github.com/mini-kep/parser-rosstat-kep/issues/24>


Contributors 
------------
- ...
- [Sergey Alexeev](https://www.upwork.com/freelancers/~013cff3deed9987cf5)
- [Jaroslav Vojtek](https://www.upwork.com/freelancers/~01eeba06021f7e72ef?viewMode=1)


Lots of good professional advice specifically in testing comes from:
- [Alexey Kryukov](https://www.upwork.com/fl/alexey) 
- [Eduard Bagrov - SYP Agency](https://www.upwork.com/freelancers/~01ce161462df65feaa) 
