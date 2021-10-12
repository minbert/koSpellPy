# pypi-template

파이썬 패키지 배포를 위한 탬플릿

# Clone this project
```
npx degit https://github.com/Kangsukmin/pypi-template your_project
cd your_project
```

# How to use

1. src/{패키지이름} 에 패키지를 만드세요

2. 필요한 모듈을 설치합니다.

```
pip install setuptools wheel twine
```

3. setup.py에 빈칸을 채우세요

4. (옵션) 사용한 모듈이 있다면, requirements.txt에 채우세요

5. 패키지를 빌드합니다.

```
python setup.py sdist bdist_wheel
```

6. 배포합니다.

```
python -m twine upload dist/*
```
