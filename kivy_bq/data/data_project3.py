#  data_project3.py

# 2) 对应的 BQ 示例回答，支持英文/中文
#   字典键： "1","2","3",...,"12"
#   值：再用 { "en": "...", "cn": "..." } 存储两种语言答案
P3_BQ_ANSWERS = {
    "1":  {"en": "Sample answer (EN) for tight deadline.",
           "cn": "示例回答（中文）：紧迫期限如何处理……"},
    "2":  {"en": "Sample answer (EN) for going above and beyond.",
           "cn": "示例回答（中文）：超出职责范围贡献……"},
    "3":  {"en": "Sample answer (EN) for conflict resolution.",
           "cn": "示例回答（中文）：指导队友与冲突处理……"},
    "4":  {"en": "Sample answer (EN) for learning something new quickly.",
           "cn": "示例回答（中文）：快速学习并上手新技术……"},
    "5":  {"en": "Sample answer (EN) for decision with incomplete info.",
           "cn": "示例回答（中文）：做出决策并承担风险……"},
    "6":  {"en": "Sample answer (EN) for fail to deliver on time.",
           "cn": "示例回答（中文）：无法完成承诺时的应对……"},
    "7":  {"en": "Sample answer (EN) for collect more info vs. start now.",
           "cn": "示例回答（中文）：在信息不足情况下快速行动……"},
    "8":  {"en": "Sample answer (EN) for a mistake you made.",
           "cn": "示例回答（中文）：做过的错误决策或操作……"},
    "9":  {"en": "Sample answer (EN) for missing a deadline.",
           "cn": "示例回答（中文）：错过截止日期……"},
    "10": {"en": "Sample answer (EN) for your proudest project.",
           "cn": "示例回答（中文）：最让你自豪的项目……"},
    "11": {"en": "Sample answer (EN) for sacrificing short term for long term.",
           "cn": "示例回答（中文）：为了长期利益而牺牲短期收益……"},
    "12": {"en": "Sample answer (EN) for dealing with a difficult team member.",
           "cn": "示例回答（中文）：与难合作团队成员相处……"}
}

# 5) 针对各 Project，各 LP 对应的 Follow-up 问题 & 答案
#   每个项目的 LP 不变，但每个项目出现的跟进问题 / 答案不一样
Project3_LP_FOLLOWUP_QUESTIONS = {
    1:  "P3 Follow-up Q: 你觉得如何让客户体验更好？",
    2:  "P3 Follow-up Q: 团队中若有人不认同主人翁精神，你怎么办？",
    # … 3 ~ 16
}
Project3_LP_FOLLOWUP_ANSWER = {
    1:  "P3 Follow-up A: 我会持续收集客户痛点，并组织团队讨论可行方案……",
    2:  "P3 Follow-up A: 先沟通背后的原因，再用实例和结果去影响对方……",
    # … 3 ~ 16
}