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
