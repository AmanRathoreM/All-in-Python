<!-- Date 10-11-2021 -->

## Coding Guidelines and Docstrings

#### Formatters
Use below command in console to scan your python code that is written according to conventions or not:
```console
pylint filename.py
```
> Note: You can also use [flake8](https://github.com/PyCQA/flake8) instead of [pylint](https://github.com/PyCQA/pylint) you can see the differences between these two python packages [here](https://www.saashub.com/compare-pylint-vs-flake8).

To make your imports according to python conventions by using [isort](https://pycqa.github.io/isort/), use below command in console:
```console
isort filename.py
```
> Note: You can also use `isort filename.py --diff` to compare differences.

You can also use [Auto-pep-8](https://github.com/hhatto/autopep8) to format your python code, use below command in console to do so:
```console
autopep8 --in-place filename.py
```
> Note: Same like isort, you can also use `autopep8 filename.py --diff` to just compare differences.
>> You can also use [black](https://github.com/psf/black) to format your code.

#### Docstrings
There are different types of docstrings formats like [sphinx style](https://www.sphinx-doc.org/en/master/), [numpy style](https://numpydoc.readthedocs.io/en/latest/format.html), or [google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). You can use any of them but [google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) is recommended.

#### Type-Annotation
[Type-Annotation](https://docs.python.org/3.9/library/typing.html) are recommend to use if you are working on a large project or if you want to reuse your code again-and-again.
[Syntax for type annotation](type_annotation.py) is as follows:
```python
def return_email(self, mail: str = "gmail") -> str:
```