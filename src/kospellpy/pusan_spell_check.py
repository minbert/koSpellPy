import requests


URL = "http://speller.cs.pusan.ac.kr/results"
headers = {"Content-Type": "application/x-www-form-urlencoded"}


def get_spell_check_info(raw_data):
    start_index = raw_data.index("data = ") + 7
    end_index = raw_data.index(";\n\tpageIdx")
    return eval(raw_data[start_index:end_index])


def get_text_and_error(spell_info):
    err_list = spell_info[0]["errInfo"]
    err_list.sort(key=lambda x: x["start"], reverse=True)
    return spell_info[0]["str"], err_list


def spell_check(text):
    res = requests.post(URL, {"text1": text})
    raw_data = res.text
    spell_info = get_spell_check_info(raw_data)
    spelled_text, err_list = get_text_and_error(spell_info)
    for error in err_list:
        if error["candWord"] != "":
            spelled_text = (
                spelled_text[: error["start"]]
                + error["candWord"].split("|")[0]
                + spelled_text[error["end"] :]
            )
    return spelled_text


if __name__ == "__main__":
    text = "검사할 텍스트"
    print(spell_check(text))
