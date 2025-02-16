#  kivy_data.py
# -*- coding: utf-8 -*-

from kivy.core.text import LabelBase
import kivy
kivy.require("2.1.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

# 1) 注册中文字体 (SimHei.ttf 仅举例, 你需在 "fonts/" 下放置该字体)
LabelBase.register(name="SimHei", fn_regular="fonts/SimHei.ttf")

class MySpinnerOption(SpinnerOption):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "SimHei"

from kivy_bq.data_imports import (
    PROJECTS_BQ_List,
    LP_List,
    LP_ANSWERS,
    P1_BQ_ANSWERS, P2_BQ_ANSWERS, P3_BQ_ANSWERS,
    Project1_LP_FOLLOWUP_QUESTIONS,
    Project1_LP_FOLLOWUP_ANSWER,
    Project2_LP_FOLLOWUP_QUESTIONS,
    Project2_LP_FOLLOWUP_ANSWER,
    Project3_LP_FOLLOWUP_QUESTIONS,
    Project3_LP_FOLLOWUP_ANSWER,
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
    return None

def safe_get_answer(data, lang_key, fallback="**[Error]** 未提供此语言回答"):
    if not data:
        return None
    if isinstance(data, dict):
        return data.get(lang_key, fallback)
    return data

def get_followup(project_key, lp_num):
    if project_key == "1":
        fu_q = Project1_LP_FOLLOWUP_QUESTIONS.get(lp_num, "暂无 follow-up 问题")
        fu_a = Project1_LP_FOLLOWUP_ANSWER.get(lp_num, "暂无 follow-up 答案")
    elif project_key == "2":
        fu_q = Project2_LP_FOLLOWUP_QUESTIONS.get(lp_num, "暂无 follow-up 问题")
        fu_a = Project2_LP_FOLLOWUP_ANSWER.get(lp_num, "暂无 follow-up 答案")
    elif project_key == "3":
        fu_q = Project3_LP_FOLLOWUP_QUESTIONS.get(lp_num, "暂无 follow-up 问题")
        fu_a = Project3_LP_FOLLOWUP_ANSWER.get(lp_num, "暂无 follow-up 答案")
    else:
        fu_q = "暂无 follow-up 问题"
        fu_a = "暂无 follow-up 答案"
    return fu_q, fu_a

class BQLayout(BoxLayout):
    answer_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 8

        # 顶部说明，用中文字体
        lbl_title = Label(
            text=("[b]Welcome to the BQ+LP Demo (Kivy) [/b]\n\n"
                  "请先选择 [color=87CEFA]Project[/color] 和 [color=87CEFA]BQ 问题[/color], "
                  "再选语言, 再用 S/T/A/R 按钮查看. 也可点击 All 查看完整回答.\n"
                  "然后可选择 [color=87CEFA]LP[/color] 并点击显示跟进问题.\n"),
            markup=True,
            halign="left",
            size_hint=(1,None),
            font_name="SimHei"  # 2) 指定中文字体
        )
        lbl_title.bind(texture_size=self._adjust_label_height)
        self.add_widget(lbl_title)

        self.add_widget(Widget(size_hint=(1,None), height=5))

        # 行1: Project + BQ + Language
        row_bq = BoxLayout(orientation="horizontal", size_hint=(1,None), height=40, spacing=8)

        row_bq.add_widget(Label(text="Project:", font_name="SimHei", size_hint=(None,1), width=70))
        self.spinner_proj = Spinner(
            text="1",
            values=PROJECT_Choices,
            size_hint=(None,1), width=60,
            font_name="SimHei",  # Spinner里text也想显示中文, 需指定
            option_cls = MySpinnerOption
        )
        row_bq.add_widget(self.spinner_proj)

        row_bq.add_widget(Label(text="BQ:", font_name="SimHei", size_hint=(None,1), width=30))
        self.spinner_bq = Spinner(
            text=PROJECTS_BQ_List[0] if PROJECTS_BQ_List else "",
            values=PROJECTS_BQ_List,
            size_hint=(0.5,1),
            font_name="SimHei",
            option_cls=MySpinnerOption
        )
        row_bq.add_widget(self.spinner_bq)

        row_bq.add_widget(Label(text="Lang:", font_name="SimHei", size_hint=(None,1), width=40))
        self.spinner_bq_lang = Spinner(
            text="English",
            values=LANG_Choices,
            size_hint=(None,1), width=80,
            font_name="SimHei",
            option_cls=MySpinnerOption

        )
        row_bq.add_widget(self.spinner_bq_lang)

        self.add_widget(row_bq)

        self.add_widget(Widget(size_hint=(1,None), height=5))

        # 行2: S/T/A/R/All
        row_star = BoxLayout(orientation="horizontal", size_hint=(1,None), height=40, spacing=5)

        btn_sit = Button(text="Situation", font_name="SimHei")
        btn_sit.bind(on_press=lambda x: self.show_bq_subfield("situation"))
        row_star.add_widget(btn_sit)

        btn_task = Button(text="Task", font_name="SimHei")
        btn_task.bind(on_press=lambda x: self.show_bq_subfield("task"))
        row_star.add_widget(btn_task)

        btn_act = Button(text="Action", font_name="SimHei")
        btn_act.bind(on_press=lambda x: self.show_bq_subfield("action"))
        row_star.add_widget(btn_act)

        btn_res = Button(text="Result", font_name="SimHei")
        btn_res.bind(on_press=lambda x: self.show_bq_subfield("result"))
        row_star.add_widget(btn_res)

        btn_all = Button(text="All", font_name="SimHei")
        btn_all.bind(on_press=lambda x: self.show_bq_subfield(None))
        row_star.add_widget(btn_all)

        self.add_widget(row_star)

        self.add_widget(Widget(size_hint=(1,None), height=10))

        # 行3: LP 选择
        row_lp = BoxLayout(orientation="horizontal", size_hint=(1,None), height=40, spacing=5)

        row_lp.add_widget(Label(text="LP:", font_name="SimHei", size_hint=(None,1), width=40))
        self.combo_lp = Spinner(
            text=LP_List[0] if LP_List else "",
            values=LP_List,
            size_hint=(0.7,1),
            font_name="SimHei",
            option_cls=MySpinnerOption
        )
        row_lp.add_widget(self.combo_lp)

        row_lp.add_widget(Label(text="LP Lang:", font_name="SimHei", size_hint=(None,1), width=60))
        self.combo_lp_lang = Spinner(
            text="English",
            values=LANG_Choices,
            size_hint=(None,1),
            width=80,
            font_name="SimHei",
            option_cls=MySpinnerOption
        )
        row_lp.add_widget(self.combo_lp_lang)

        btn_show_lp = Button(text="显示LP+Followup", font_name="SimHei")
        btn_show_lp.bind(on_press=lambda x: self.show_lp_answer())
        row_lp.add_widget(btn_show_lp)

        self.add_widget(row_lp)

        self.add_widget(Widget(size_hint=(1,None), height=10))

        # 回答显示区域
        scroll = ScrollView(size_hint=(1,1))
        self.lbl_answer = Label(
            text=self.answer_text,
            size_hint_y=None,
            markup=True,
            halign="left",
            valign="top",
            font_name="SimHei"  # 3) 显示中文回答
        )
        self.lbl_answer.bind(texture_size=self._on_texture_size)
        scroll.add_widget(self.lbl_answer)
        self.add_widget(scroll)

    def _adjust_label_height(self, instance, size):
        instance.text_size = (instance.width, None)
        instance.height = instance.texture_size[1] + 10

    def _on_texture_size(self, *args):
        self.lbl_answer.text_size = (self.lbl_answer.width, None)
        self.lbl_answer.height = self.lbl_answer.texture_size[1] + 10

    # BQ 显示
    def show_bq_subfield(self, subfield):
        project_key = self.spinner_proj.text
        bq_text = self.spinner_bq.text
        lang_str = self.spinner_bq_lang.text

        if not bq_text:
            self.answer_text = "[color=ff0000]No BQ selected[/color]"
            self.lbl_answer.text = self.answer_text
            return

        q_id = bq_text.split('.')[0].strip()
        data = get_project_bq_data(project_key, q_id)
        if not data:
            self.answer_text = f"[color=ff0000][b]Error:[/b][/color] Project {project_key} 无 BQ {q_id}"
            self.lbl_answer.text = self.answer_text
            return

        lang_key = "en" if lang_str == "English" else "cn"
        answer_data = safe_get_answer(data, lang_key)

        if answer_data is None:
            self.answer_text = f"[color=ff0000][b]Error:[/b][/color] BQ {q_id} 未提供 {lang_str} 回答"
            self.lbl_answer.text = self.answer_text
            return

        if isinstance(answer_data, dict):
            sit = answer_data.get("situation", "")
            tas = answer_data.get("task", "")
            act = answer_data.get("action", "")
            res = answer_data.get("result", "")

            if subfield == "situation":
                self.answer_text = f"[b]Situation:[/b]\n\n{sit}"
            elif subfield == "task":
                self.answer_text = f"[b]Task:[/b]\n\n{tas}"
            elif subfield == "action":
                self.answer_text = f"[b]Action:[/b]\n\n{act}"
            elif subfield == "result":
                self.answer_text = f"[b]Result:[/b]\n\n{res}"
            else:
                self.answer_text = (
                    f"[b]Situation:[/b]\n\n{sit}\n\n"
                    f"[b]Task:[/b]\n\n{tas}\n\n"
                    f"[b]Action:[/b]\n\n{act}\n\n"
                    f"[b]Result:[/b]\n\n{res}"
                )
        else:
            self.answer_text = answer_data

        self.lbl_answer.text = self.answer_text

    # LP 显示
    def show_lp_answer(self):
        from markdown2 import markdown
        project_key = self.spinner_proj.text
        lp_text = self.combo_lp.text
        lang_str = self.combo_lp_lang.text

        if not lp_text:
            self.answer_text = "[color=ff0000]No LP selected[/color]"
            self.lbl_answer.text = self.answer_text
            return

        try:
            lp_num = int(lp_text.split('.')[0].strip())
        except:
            lp_num = None

        if not lp_num or lp_num not in LP_ANSWERS:
            self.answer_text = f"[color=ff0000][b]Error:[/b][/color] 未找到 LP {lp_text} 的回答"
            self.lbl_answer.text = self.answer_text
            return

        lang_key = "en" if lang_str == "English" else "cn"
        lp_data = LP_ANSWERS[lp_num]
        lp_md = safe_get_answer(lp_data, lang_key, fallback=f"**[Error]** LP {lp_num} 未提供 {lang_str} 回答")

        if not isinstance(lp_md, str):
            self.answer_text = f"[color=ff0000][b]Error:[/b][/color] LP 数据格式异常."
            self.lbl_answer.text = self.answer_text
            return

        # follow up
        fu_q, fu_a = get_followup(project_key, lp_num)

        md_text = (
            f"{lp_md}\n\n---\n\n"
            f"**Follow-up Question:**\n\n{fu_q}\n\n"
            f"**Follow-up Answer:**\n\n{fu_a}"
        )
        # 转 markdown -> html
        html = markdown(md_text)
        self.lbl_answer.text = html


from kivy.app import App

class BQApp(App):
    def build(self):
        return BQLayout()


if __name__ == "__main__":
    BQApp().run()
