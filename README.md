[한국어 문서](./README_ko.md)

# pypi-template

Template for python package

# Clone this project
```
npx degit https://github.com/Kangsukmin/pypi-template your_project
cd your_project
```

# How to use

1. Make your package in src/{package_name}

2. Install some packages

```
pip install setuptools wheel twine
```

3. Fill in the blanks on setup.py

4. (Optional) If you want to add dependencies, Fill those in requirements.txt

5. Build your package

```
python setup.py sdist bdist_wheel
```

6. Upload your package

```
python -m twine upload dist/*
```
