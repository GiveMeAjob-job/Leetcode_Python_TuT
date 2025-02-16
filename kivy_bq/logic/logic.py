# logic/logic.py
# -*- coding: utf-8 -*-

import sys

# 如果你想在 logic.py 中也访问 PROJECTS_BQ_List 等，可以：
# from bq.data_imports import (
#     PROJECTS_BQ_List,
#     ...
# )
import markdown2



from bq.data_imports import (
    P1_BQ_ANSWERS,
    P2_BQ_ANSWERS,
    P3_BQ_ANSWERS,
)

def get_project_bq_data(project_key, q_identifier):
    """
    根据 project_key（"1"/"2"/"3"）和 BQ 问题编号（"1"~"12"），
    返回对应的回答数据（可能是 dict，也可能是 str）。
    """
    if project_key == "1":
        return P1_BQ_ANSWERS.get(q_identifier)
    elif project_key == "2":
        return P2_BQ_ANSWERS.get(q_identifier)
    elif project_key == "3":
        return P3_BQ_ANSWERS.get(q_identifier)
    else:
        return None

def safe_get_answer(data, lang_key, fallback="**[Error]** 未提供此语言回答"):
    """
    安全获取多语言回答:
      - 如果 data 是 dict，则取 data[lang_key]，若不存在则返回 fallback
      - 如果 data 是 str，则说明只有单个回答，直接返回该 str
      - 如果 data 是 None，则也返回 fallback
    """
    if not data:
        return fallback
    if isinstance(data, dict):
        return data.get(lang_key, fallback)
    return str(data)

