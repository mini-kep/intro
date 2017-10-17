Testing guidelines
==================

These guidelines cover unit tests (being) developped at various parts of ```mini-kep``` project.

We do not have functional (eg selenium) or load tests, which may have slightly different logic. 

Introduction
------------

Testing is known to be even harder than writing original code. 

When testing one must think of:

a) program behaviours
- how the code under test is supposed to run well 
- how the code under test may run with error
- how to expose behaviours above in test setup and checks?


b) clean tests
- how to write test in a clean and understandable fashion? 
- how to name tests better?
- how to make tests small?

c) test efficiency
- what conditions/arguements/contexts are most probable for the code under test?
- what happens in program outside code under test?


Checklist
----------

Best tests:
1. run quick and often
2. use a continious integration like Travis CI and use coverage metrics like codecov 
3. cover at least all public methods/functions
4. have long names with context and expected result (except very short tests)
5. are as simple and readable as they can get
6. one test tests one thing and better if it has one assert per test
7. have clear separation of setup, call of code under test and check 
8. make good use of parametrisation, factories/fixtures, dependency injection, mocks and monkey-patching
9. concentrate around practical risks in program execution, not fantasy situations  
10. include just a few integration, end-to-end tests
11. fail early and near where problem is
12. are usually assmebled in one testcase class for a single class or model

Learning
--------
Basic testing in python:
- <http://docs.python-guide.org/en/latest/writing/tests/>

Takeaways from <https://pylonsproject.org/community-unit-testing-guidelines.html>:
- tests should be as simple as possible
- tests should be isolated
- each test method should test Just One Thing

Very consise guide: <https://gist.github.com/sloria/7001839#testing>

Test naming
-----------

Tests have to be named properly and clearly tell:
- what function or method is tested
- what input or context is given
- what is the expected result or behaviour


```
[the name of the tested method]_[expected input / tested state]_[expected behavior]

[expected behavior] is usually [returns_something | raises_something | ...]
```
   

Comments:
  - smaller tests can have simplier naming. Better a ```test_make_date()``` or
    ```test_to_float_accepts_commented_string``` than no test at all  
  - regression test (bugfixes) can have names stating what the problem was, eg ```test_CBR_USD_will_not_work_before_1992```
  - read about *Arrange-Act-Assert* or *Given-When-Then* for more information, <https://stackoverflow.com/questions/155436/unit-test-naming-best-practices> is oftern cited for naming, but discussion has some controversies. 

To cover 
--------
- testing is not the best technique to ensure code quality (eg reviews)
- testing in flask with db

Prior discussions
-----------------
- Flask testing: <https://github.com/mini-kep/frontend-app/issues/7>
- parsers testing: <https://github.com/mini-kep/parsers/issues/15>
- earlier on parsers testing: <https://github.com/mini-kep/parser-rosstat-kep/issues/24>
- <https://github.com/epogrebnyak/question-kep-unittest>


Contributors 
------------
- [Sergey Alexeev](https://www.upwork.com/freelancers/~013cff3deed9987cf5)
- [Jaroslav Vojtek](https://www.upwork.com/freelancers/~01eeba06021f7e72ef?viewMode=1)


Specialised advice 
------------------
I got lots of  professional advice specifically in testing from:
- [Alexey Kryukov](https://www.upwork.com/fl/alexey) 
- [Eduard Bagrov - SYP Agency](https://www.upwork.com/freelancers/~01ce161462df65feaa) 

These people are highly recommended to work with. 
