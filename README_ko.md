# koSpellPy

한국어 맞춤법 검사기

# 사용법

## 설치

```
pip install kospellpy
```

## 사용

```python
from kospellpy import spell_init

spell_checker = spell_init() # 기본값으로 부산대학교 맞춤법 검사기를 사용합니다.
                             # 네이버 맞춤법 검사기를 사용하시려면 spell_init('naver') 를 사용하세요

text = "인공지능이너무 재밓따!"

print(spell_checker(text))
>> 인공지능이 너무 재밌다!
```
