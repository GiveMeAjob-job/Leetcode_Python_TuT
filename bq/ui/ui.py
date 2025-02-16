# ui/ui.py
# -*- coding: utf-8 -*-

import sys
import markdown2
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextBrowser, QComboBox,
    QGroupBox, QSpacerItem, QSizePolicy
)

from PyQt5.QtCore import Qt

# 从 data_imports 中拿到 PROJECTS_BQ_List, LP_List, LP_ANSWERS, etc
from bq.data_imports import (
    PROJECTS_BQ_List,
    LP_List,
    LP_ANSWERS,
    Project1_LP_FOLLOWUP_QUESTIONS,
    Project1_LP_FOLLOWUP_ANSWER,
    Project2_LP_FOLLOWUP_QUESTIONS,
    Project2_LP_FOLLOWUP_ANSWER,
    Project3_LP_FOLLOWUP_QUESTIONS,
    Project3_LP_FOLLOWUP_ANSWER,
)
# 从 logic 中导入函数
from bq.logic.logic import get_project_bq_data, safe_get_answer

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BQ + LP Demo (PyQt Markdown) — S/T/A/R 拆分")
        self.init_ui()

    def init_ui(self):
        """
        构建界面布局
        """
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(10)

        # ------ 顶部标题/说明 ------
        lbl_title = QLabel("Welcome to the BQ + LP Demo!\n\n"
                           "请先选择 Project 和 BQ 问题，再选择语言，然后使用下方按钮查看 S/T/A/R 或完整回答。\n"
                           "也可以选择 LP 并查看对应 Follow-up 问题与答案。")
        lbl_title.setAlignment(Qt.AlignLeft)
        lbl_title.setStyleSheet("font-size: 14px; font-weight: bold;")
        main_layout.addWidget(lbl_title)

        # ------ BQ 选择分组 ------
        gb_bq = QGroupBox("BQ 问题选择与语言")
        gb_bq_layout = QVBoxLayout(gb_bq)

        # 行1: Project 选择
        row_project = QHBoxLayout()
        label_proj = QLabel("选择 Project:")
        self.combo_project = QComboBox()
        self.combo_project.addItems(["1", "2", "3"])
        row_project.addWidget(label_proj)
        row_project.addWidget(self.combo_project)
        gb_bq_layout.addLayout(row_project)

        # 行2: BQ 问题选择 + 语言
        row_bq = QHBoxLayout()
        label_bq = QLabel("选择 BQ 问题:")
        self.combo_bq = QComboBox()
        self.combo_bq.addItems(PROJECTS_BQ_List)  # 12道 BQ
        row_bq.addWidget(label_bq)
        row_bq.addWidget(self.combo_bq)

        self.combo_bq_lang = QComboBox()
        self.combo_bq_lang.addItems(["English", "中文"])
        row_bq.addWidget(self.combo_bq_lang)

        gb_bq_layout.addLayout(row_bq)
        main_layout.addWidget(gb_bq)

        # ------ 按钮分组: S/T/A/R/完整回答 ------
        gb_star = QGroupBox("S/T/A/R / 完整回答")
        gb_star_layout = QHBoxLayout(gb_star)

        self.btn_situation = QPushButton("Situation")
        self.btn_situation.setToolTip("查看 BQ 回答中的「Situation」部分")
        self.btn_situation.clicked.connect(lambda: self.show_bq_subfield("situation"))
        gb_star_layout.addWidget(self.btn_situation)

        self.btn_task = QPushButton("Task")
        self.btn_task.setToolTip("查看 BQ 回答中的「Task」部分")
        self.btn_task.clicked.connect(lambda: self.show_bq_subfield("task"))
        gb_star_layout.addWidget(self.btn_task)

        self.btn_action = QPushButton("Action")
        self.btn_action.setToolTip("查看 BQ 回答中的「Action」部分")
        self.btn_action.clicked.connect(lambda: self.show_bq_subfield("action"))
        gb_star_layout.addWidget(self.btn_action)

        self.btn_result = QPushButton("Result")
        self.btn_result.setToolTip("查看 BQ 回答中的「Result」部分")
        self.btn_result.clicked.connect(lambda: self.show_bq_subfield("result"))
        gb_star_layout.addWidget(self.btn_result)

        self.btn_full = QPushButton("完整回答")
        self.btn_full.setToolTip("查看 BQ 回答的全部四个部分")
        self.btn_full.clicked.connect(lambda: self.show_bq_subfield(None))  # None => 全拼
        gb_star_layout.addWidget(self.btn_full)

        main_layout.addWidget(gb_star)

        # ------ LP 选择分组 ------
        gb_lp = QGroupBox("LP 选择与 Follow-up")
        gb_lp_layout = QVBoxLayout(gb_lp)

        row_lp = QHBoxLayout()
        label_lp = QLabel("选择 LP:")
        self.combo_lp = QComboBox()
        for item in LP_List:
            self.combo_lp.addItem(item)
        row_lp.addWidget(label_lp)
        row_lp.addWidget(self.combo_lp)

        self.combo_lp_lang = QComboBox()
        self.combo_lp_lang.addItems(["English", "中文"])
        row_lp.addWidget(self.combo_lp_lang)

        self.btn_show_lp = QPushButton("显示 LP 回答 + Follow-up")
        self.btn_show_lp.setToolTip("查看所选 LP 的回答和跟进问题")
        self.btn_show_lp.clicked.connect(self.show_lp_answer)
        row_lp.addWidget(self.btn_show_lp)

        gb_lp_layout.addLayout(row_lp)
        main_layout.addWidget(gb_lp)

        # ------ 放大/缩小 ------
        row_zoom = QHBoxLayout()
        self.btn_zoom_in = QPushButton("放大")
        self.btn_zoom_in.setToolTip("放大回答显示字体")
        self.btn_zoom_in.clicked.connect(lambda: self.browser.zoomIn(1))

        self.btn_zoom_out = QPushButton("缩小")
        self.btn_zoom_out.setToolTip("缩小回答显示字体")
        self.btn_zoom_out.clicked.connect(lambda: self.browser.zoomOut(1))

        row_zoom.addWidget(self.btn_zoom_in)
        row_zoom.addWidget(self.btn_zoom_out)
        row_zoom.addStretch()  # 占位让按钮在左，空白在右

        main_layout.addLayout(row_zoom)

        # ------ 文本显示区域 ------
        self.browser = QTextBrowser()
        main_layout.addWidget(self.browser)

        self.setLayout(main_layout)

    def show_bq_subfield(self, subfield):
        project_key = self.combo_project.currentText()  # "1","2","3"
        bq_text = self.combo_bq.currentText()           # e.g. "1. 紧迫期限..."
        lang_str = self.combo_bq_lang.currentText()

        # "1"
        q_identifier = bq_text.split('.')[0].strip()
        data = get_project_bq_data(project_key, q_identifier)

        if not data:
            md_text = f"**[Error]** 在 Project {project_key} 中找不到 BQ 问题 {q_identifier} 的回答。"
        else:
            lang_key = "en" if lang_str == "English" else "cn"
            data_for_lang = safe_get_answer(data, lang_key,
                fallback=f"**[Error]** BQ {q_identifier} 未提供 {lang_str} 回答")

            if isinstance(data_for_lang, dict):
                sit = data_for_lang.get("situation","")
                tas = data_for_lang.get("task","")
                act = data_for_lang.get("action","")
                res = data_for_lang.get("result","")

                if subfield == "situation":
                    md_text = f"## Situation\n\n{sit}"
                elif subfield == "task":
                    md_text = f"## Task\n\n{tas}"
                elif subfield == "action":
                    md_text = f"## Action\n\n{act}"
                elif subfield == "result":
                    md_text = f"## Result\n\n{res}"
                else:
                    md_text = (f"## Situation\n\n{sit}\n\n"
                               f"## Task\n\n{tas}\n\n"
                               f"## Action\n\n{act}\n\n"
                               f"## Result\n\n{res}")
            else:
                # 如果 data_for_lang 是字符串，不拆 S/T/A/R
                md_text = str(data_for_lang)

        html = markdown2.markdown(md_text)
        self.browser.setHtml(html)

    def show_lp_answer(self):
        project_key = self.combo_project.currentText()
        lp_text = self.combo_lp.currentText()
        lang_str = self.combo_lp_lang.currentText()

        lp_num_str = lp_text.split('.')[0].strip()
        try:
            lp_num = int(lp_num_str)
        except ValueError:
            lp_num = None

        if lp_num is None or lp_num not in LP_ANSWERS:
            md_text = f"**[Error]** 没有找到 LP {lp_text} 的示例回答。"
        else:
            lang_key = "en" if lang_str == "English" else "cn"
            lp_data = LP_ANSWERS[lp_num]
            lp_md = safe_get_answer(lp_data, lang_key,
                fallback=f"**[Error]** LP {lp_num} 未提供 {lang_str} 回答。")

            # 根据 project_key 获取 follow-up
            if project_key == "1":
                fu_q = Project1_LP_FOLLOWUP_QUESTIONS.get(lp_num, "暂无 follow-up 问题")
                fu_a = Project1_LP_FOLLOWUP_ANSWER.get(lp_num, "暂无 follow-up 答案")
            elif project_key == "2":
                fu_q = Project2_LP_FOLLOWUP_QUESTIONS.get(lp_num, "暂无 follow-up 问题")
                fu_a = Project2_LP_FOLLOWUP_ANSWER.get(lp_num, "暂无 follow-up 答案")
            else:
                fu_q = Project3_LP_FOLLOWUP_QUESTIONS.get(lp_num, "暂无 follow-up 问题")
                fu_a = Project3_LP_FOLLOWUP_ANSWER.get(lp_num, "暂无 follow-up 答案")

            md_text = (
                f"{lp_md}\n\n---\n\n"
                f"**Follow-up Question:**\n\n{fu_q}\n\n"
                f"**Follow-up Answer:**\n\n{fu_a}"
            )

        html = markdown2.markdown(md_text)
        self.browser.setHtml(html)
