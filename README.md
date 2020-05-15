# Pymuse

Library for musical theory analysis

## Getting Started

```
[~/]$ git clone https://github.com/yodestarn/pymuse
[~/]$ cd pymuse
```

### Prerequisites

Python 3 virtual environment is recommended.

Here are simple steps to get one working:
```
[~/pymuse]$ python3 -m virtualenv pymuse-venv
[~/pymuse]$ source pymuse-venv/bin/activate
(pymuse-venv) [~/pymuse]$ pip install -r requirements.txt
```

### Installing

```
[~/]$ cd pymuse
[~/pymuse]$ python setup.py develop
[~/pymuse]$ cd ../..
[/home]$ python
Python 3.x.x (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) XXXXXXXXXXXXXXXXXXXXXXX
Type "help", "copyright", "credits" or "license" for more information.
>>> import pymuse
>>> from pymuse import Scale
>>> s = Scale(0)
>>> print s
C
>>> for n in s:
...   print(pymuse.Note(n))
...
C
D
E
F
G
A
B
```

## Running the tests

```
[~/projects/pymuse]$ make test
```

## Authors

* **PREVOST Corentin** - *Initial work*

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details
