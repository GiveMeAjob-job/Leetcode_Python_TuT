# main.py
# -*- coding: utf-8 -*-

import kivy
kivy.require("2.1.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.uix.widget import Widget  # 用于插入空白占位

# 假设你已有 data_imports.py, 里定义了下列函数和数据：
from bq.data_imports import (
    PROJECTS_BQ_List,  # ["1. 紧迫期限","2. 超出职责...", ...]
    P1_BQ_ANSWERS,
    P2_BQ_ANSWERS,
    P3_BQ_ANSWERS,
)

PROJECT_Choices = ["1","2","3"]
LANG_Choices = ["English","中文"]

def get_project_bq_data(project_key, q_identifier):
    if project_key == "1":
        return P1_BQ_ANSWERS.get(q_identifier)
    elif project_key == "2":
        return P2_BQ_ANSWERS.get(q_identifier)
    elif project_key == "3":
        return P3_BQ_ANSWERS.get(q_identifier)
    else:
        return None

def safe_get_answer(data, lang_key):
    if not data:
        return None
    return data.get(lang_key)

class BQLayout(BoxLayout):
    answer_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        # 给主布局设置一定的内边距和控件间距
        self.padding = 10
        self.spacing = 8

        # ============ 顶部说明 Label ============
        # 不固定高度, 让文字可自动换行
        lbl_instructions = Label(
            text=(
                "[b]Welcome to the BQ Demo![/b]\n\n"
                "请选择 [color=87CEFA]Project[/color] 和 [color=87CEFA]BQ问题[/color], "
                "再选择语言, 然后点击 S/T/A/R/All 按钮查看对应回答. \n"
                "回答是用 [b]BBCode[/b] 标记进行简单渲染. \n"
            ),
            markup=True,
            size_hint=(1, None),
            halign="left",
        )
        # 让 Label 随文本自动高度
        lbl_instructions.bind(texture_size=self._adjust_label_height)
        self.add_widget(lbl_instructions)

        # ============ 在标题和下方加一个空白占位，增添间距 ============
        spacer_top = Widget(size_hint=(1, None), height=10)
        self.add_widget(spacer_top)

        # ============ 第一行: Project + BQ + Language ============
        row_top = BoxLayout(orientation="horizontal", size_hint=(1, None), height=40, spacing=10)

        # Project
        lbl_proj = Label(text="Project:", size_hint=(None,1), width=70)
        row_top.add_widget(lbl_proj)
        self.spinner_proj = Spinner(text="1", values=PROJECT_Choices, size_hint=(None,1), width=60)
        row_top.add_widget(self.spinner_proj)

        # BQ
        lbl_bq = Label(text=" BQ:", size_hint=(None,1), width=30)
        row_top.add_widget(lbl_bq)
        self.spinner_bq = Spinner(
            text=PROJECTS_BQ_List[0] if PROJECTS_BQ_List else "",
            values=PROJECTS_BQ_List,
            size_hint=(0.6,1),
        )
        row_top.add_widget(self.spinner_bq)

        # Lang
        lbl_lang = Label(text="Lang:", size_hint=(None,1), width=40)
        row_top.add_widget(lbl_lang)
        self.spinner_lang = Spinner(text="English", values=LANG_Choices, size_hint=(None,1), width=80)
        row_top.add_widget(self.spinner_lang)

        self.add_widget(row_top)

        # ============ 第二行: S/T/A/R/All 按钮 ============
        spacer_between = Widget(size_hint=(1, None), height=10)
        self.add_widget(spacer_between)

        row_buttons = BoxLayout(orientation="horizontal", size_hint=(1, None), height=40, spacing=5)

        btn_sit = Button(text="Situation")
        btn_sit.bind(on_press=lambda x: self.show_subfield("situation"))
        row_buttons.add_widget(btn_sit)

        btn_task = Button(text="Task")
        btn_task.bind(on_press=lambda x: self.show_subfield("task"))
        row_buttons.add_widget(btn_task)

        btn_action = Button(text="Action")
        btn_action.bind(on_press=lambda x: self.show_subfield("action"))
        row_buttons.add_widget(btn_action)

        btn_result = Button(text="Result")
        btn_result.bind(on_press=lambda x: self.show_subfield("result"))
        row_buttons.add_widget(btn_result)

        btn_all = Button(text="All")
        btn_all.bind(on_press=lambda x: self.show_subfield(None))
        row_buttons.add_widget(btn_all)

        self.add_widget(row_buttons)

        # ============ 第三行: ScrollView + Label 显示回答 ============
        spacer_between2 = Widget(size_hint=(1, None), height=10)
        self.add_widget(spacer_between2)

        scroll = ScrollView(size_hint=(1,1))
        self.lbl_answer = Label(
            text=self.answer_text,
            size_hint_y=None,
            markup=True,
            halign="left",
            valign="top"
        )
        self.lbl_answer.bind(texture_size=self._on_texture_size)
        scroll.add_widget(self.lbl_answer)
        self.add_widget(scroll)

    def _adjust_label_height(self, instance, size):
        """让顶部说明Label能自适应内容多行高度"""
        instance.text_size = (instance.width, None)  # 让文字基于label宽度进行换行
        instance.height = instance.texture_size[1] + 10

    def _on_texture_size(self, *args):
        """让回答Label自适应文本高度"""
        self.lbl_answer.text_size = (self.lbl_answer.width, None)
        self.lbl_answer.height = self.lbl_answer.texture_size[1] + 10

    def show_subfield(self, subfield):
        project_key = self.spinner_proj.text
        bq_str = self.spinner_bq.text
        lang = self.spinner_lang.text

        if not bq_str:
            self.answer_text = "[color=ff0000]No BQ selected[/color]"
            self.lbl_answer.text = self.answer_text
            return

        q_identifier = bq_str.split('.')[0].strip()

        data_dict = get_project_bq_data(project_key, q_identifier)
        if not data_dict:
            self.answer_text = f"[b][color=ff0000]Error:[/color][/b] Project {project_key} 无 BQ {q_identifier}"
            self.lbl_answer.text = self.answer_text
            return

        data_for_lang = safe_get_answer(data_dict, "en" if lang=="English" else "cn")
        if not data_for_lang:
            self.answer_text = f"[b][color=ff0000]Error:[/color][/b] BQ {q_identifier} 没有 {lang} 回答"
            self.lbl_answer.text = self.answer_text
            return

        # 判断是否是 dict
        if isinstance(data_for_lang, dict):
            sit = data_for_lang.get("situation", "")
            tas = data_for_lang.get("task", "")
            act = data_for_lang.get("action", "")
            res = data_for_lang.get("result", "")

            if subfield == "situation":
                self.answer_text = f"[b]Situation:[/b]\n\n{sit}"
            elif subfield == "task":
                self.answer_text = f"[b]Task:[/b]\n\n{tas}"
            elif subfield == "action":
                self.answer_text = f"[b]Action:[/b]\n\n{act}"
            elif subfield == "result":
                self.answer_text = f"[b]Result:[/b]\n\n{res}"
            else:
                # All
                self.answer_text = (
                    f"[b]Situation:[/b]\n\n{sit}\n\n"
                    f"[b]Task:[/b]\n\n{tas}\n\n"
                    f"[b]Action:[/b]\n\n{act}\n\n"
                    f"[b]Result:[/b]\n\n{res}"
                )
        else:
            # 纯字符串
            self.answer_text = data_for_lang

        self.lbl_answer.text = self.answer_text


class BQApp(App):
    def build(self):
        return BQLayout()


if __name__ == "__main__":
    BQApp().run()
