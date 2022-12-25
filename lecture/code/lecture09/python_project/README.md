# A simple Python project for CS107/AC207

Demonstration of PEP517 and PEP518 for package building and distribution.

> See [https://packaging.python.org/tutorials/packaging-projects/](https://packaging.python.org/tutorials/packaging-projects/)

## Steps

1. Clean previous distributions: `rm dist/*`
2. Build the package release: `python -m build .`
3. Upload to [test.pypi.org](test.pypi.org): `twine upload --repository testpypi dist/*`
4. Repo: [https://test.pypi.org/project/Fall2022-CS107/](https://test.pypi.org/project/Fall2022-CS107/)

## Installing the package

```bash
python -m pip install -i https://test.pypi.org/simple/ Fall2022_CS107
```
