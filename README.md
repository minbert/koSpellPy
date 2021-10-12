[한국어 문서](./README_ko.md)

# koSpellPy

Korean Spell checker

# How to use

## Install

```
pip install kospellpy
```

## Use

```python
from kospellpy import spell_init

spell_checker = spell_init() # default: busan spell check
                             # if you want to use naver_spell_check, just use spell_init('naver')

text = "인공지능이너무 재밓따!"

print(spell_checker(text))
>> 인공지능이 너무 재밌다!
```
