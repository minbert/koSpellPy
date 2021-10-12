from .pusan_spell_check import spell_check as pusan_spell_check
from .naver_spell_check import spell_check as naver_spell_check


def spell_init(product="pusan"):
    if product == "pusan":
        return pusan_spell_check
    elif product == "naver":
        return naver_spell_check
    else:
        raise "product must be pusan or naver"
