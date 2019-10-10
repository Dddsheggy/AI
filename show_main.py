from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main import Ui_Form
import show_warning
import show_correct
import show_wInput
import match1
import random
import sys


class mywindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.setup_button()
        self.setup_look()
        self.Again.clicked.connect(self.playAgain)
        self.answerPool = set()
        self.yourA = ''
        self.sysQ = ''
        self.ui1 = show_correct.mywindow()
        self.ui2 = show_warning.mywindow1()
        self.ui3 = show_wInput.mywindow()
        self.play()

    def setup_look(self):
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('火柴等式')
        self.setFixedSize(self.width(), self.height())

        png = QtGui.QPixmap('icon.png').scaled(self.decorate.width(), self.decorate.height())
        self.decorate.setPixmap(png )

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setup_button(self):
        self.is_Input.setCheckable(True)
        self.no_Input.setCheckable(True)
        self.is_choose.setCheckable(True)
        self.level_1.setCheckable(True)
        self.level_2.setCheckable(True)
        self.level_3.setCheckable(True)
        self.begin_yourQA.setCheckable(True)
        self.Again.setCheckable(True)
        self.inputing_QA.setMaxLength(12)
        self.inputing_QA.setEnabled(False)
        self.begin_yourQA.setEnabled(False)
        self.level_1.setEnabled(False)
        self.level_2.setEnabled(False)
        self.level_3.setEnabled(False)

    def play(self):
        self.is_Input.clicked.connect(self.play_Input)
        self.no_Input.clicked.connect(self.play_Sys)
        self.is_choose.clicked.connect(self.play_Choose)

    def play_Input(self):
        self.is_Input.setChecked(False)
        self.is_Input.setEnabled(False)
        self.no_Input.setEnabled(False)
        self.is_choose.setEnabled(False)
        self.inputing_QA.setEnabled(True)
        self.begin_yourQA.setEnabled(True)
        self.Again.setEnabled(False)
        self.input_QA.setText('请输入问题')
        self.begin_yourQA.clicked.connect(self.judge)

    def judge(self):
        self.begin_yourQA.setChecked(False)
        Match0 = match1.Match()
        Match0.make_M()
        preTest = Match0.preTest(str(self.inputing_QA.text()))
        if preTest == 1:
            self.ui1.setWindowModality(Qt.ApplicationModal)
            self.ui1.show()
            self.inputing_QA.clear()
        elif preTest == 2:
            self.ui2.setWindowModality(Qt.ApplicationModal)
            self.ui2.show()
            self.inputing_QA.clear()
        elif preTest == 0:
            self.ui3.setWindowModality(Qt.ApplicationModal)
            self.ui3.show()
            self.inputing_QA.clear()
        else:
            self.answerPool = preTest
            self.show_Q.setText('问题为')
            self.Q.setText(self.inputing_QA.text())
            self.inputing_QA.clear()
            self.input_QA.setText('请输入答案')
            self.begin_yourQA.disconnect()
            self.begin_yourQA.clicked.connect(self.Input_ans)

    def Input_ans(self):
        self.begin_yourQA.setChecked(False)
        self.begin_yourQA.setEnabled(False)
        self.show_your_A.setText('你的答案为')
        self.your_A.setText(self.inputing_QA.text())
        self.yourA = str(self.inputing_QA.text())
        self.inputing_QA.clear()
        self.input_QA.clear()
        self.inputing_QA.setEnabled(False)
        if self.yourA in self.answerPool:
            self.judgement.setText('恭喜你！回答正确！')
            self.show_sys_A.setText('其他答案')
            text1 = ''
            for i in self.answerPool:
                if i != self.yourA:
                    text1 += i + '\n'
            self.sys_A.setText(text1)
        else:
            self.judgement.setText('很遗憾！回答错误！')
            self.show_sys_A.setText('正确答案')
            text = ''
            for i in self.answerPool:
                text += i + '\n'
            self.sys_A.setText(text)
        self.Again.setEnabled(True)
        self.begin_yourQA.disconnect()

    def playAgain(self):
        self.Again.setChecked(False)
        self.inputing_QA.setEnabled(False)
        self.begin_yourQA.setEnabled(False)
        self.is_Input.setEnabled(True)
        self.no_Input.setEnabled(True)
        self.is_choose.setEnabled(True)
        self.level_1.setEnabled(False)
        self.level_2.setEnabled(False)
        self.level_3.setEnabled(False)
        self.show_Q.clear()
        self.Q.clear()
        self.show_your_A.clear()
        self.your_A.clear()
        self.judgement.clear()
        self.show_sys_A.clear()
        self.sys_A.clear()
        self.answerPool = set()
        self.yourA = ''
        self.sysQ = ''
        self.play()

    def play_Choose(self):
        self.is_choose.setChecked(False)
        self.is_choose.setEnabled(False)
        self.level_1.setEnabled(True)
        self.level_2.setEnabled(True)
        self.level_3.setEnabled(True)
        self.level_1.clicked.connect(self.choose_L11)
        self.level_2.clicked.connect(self.choose_L22)
        self.level_3.clicked.connect(self.choose_L33)
        self.is_Input.setEnabled(False)
        self.no_Input.setEnabled(False)
        self.Again.setEnabled(False)

    def choose_L11(self):
        self.level_1.setChecked(False)
        self.level_1.setEnabled(False)
        self.level_2.setEnabled(False)
        self.level_3.setEnabled(False)
        Match1 = match1.Match()
        Match1.make_M()
        self.sysQ = '3+3=0'
        self.show_Q.setText('问题为')
        self.Q.setText(self.sysQ)
        self.answerPool = Match1.solve(self.sysQ)
        self.input_QA.setText('请输入答案')
        self.inputing_QA.setEnabled(True)
        self.begin_yourQA.setEnabled(True)
        self.level_1.disconnect()
        self.begin_yourQA.clicked.connect(self.Sys_A)

    def choose_L22(self):
        self.level_2.setChecked(False)
        self.level_1.setEnabled(False)
        self.level_2.setEnabled(False)
        self.level_3.setEnabled(False)
        Match1 = match1.Match()
        Match1.make_M()
        self.sysQ = '6+4=4'
        self.show_Q.setText('问题为')
        self.Q.setText(self.sysQ)
        self.answerPool = Match1.solve(self.sysQ)
        self.input_QA.setText('请输入答案')
        self.inputing_QA.setEnabled(True)
        self.begin_yourQA.setEnabled(True)
        self.level_2.disconnect()
        self.begin_yourQA.clicked.connect(self.Sys_A)

    def choose_L33(self):
        self.level_3.setChecked(False)
        self.level_1.setEnabled(False)
        self.level_2.setEnabled(False)
        self.level_3.setEnabled(False)
        Match1 = match1.Match()
        Match1.make_M()
        self.sysQ = '45+46=99'
        self.show_Q.setText('问题为')
        self.Q.setText(self.sysQ)
        self.answerPool = Match1.solve(self.sysQ)
        self.input_QA.setText('请输入答案')
        self.inputing_QA.setEnabled(True)
        self.begin_yourQA.setEnabled(True)
        self.level_3.disconnect()
        self.begin_yourQA.clicked.connect(self.Sys_A)

    def Choose_A(self):
        self.begin_yourQA.setChecked(False)
        self.begin_yourQA.setEnabled(False)
        self.show_your_A.setText('你的答案为')
        self.your_A.setText(self.inputing_QA.text())
        self.yourA = str(self.inputing_QA.text())
        self.inputing_QA.clear()
        self.input_QA.clear()
        self.inputing_QA.setEnabled(False)
        if self.yourA in self.answerPool:
            self.judgement.setText('恭喜你！回答正确！')
            self.show_sys_A.setText('其他答案')
            text1 = ''
            for i in self.answerPool:
                if i != self.yourA:
                    text1 += i + '\n'
            self.sys_A.setText(text1)
        else:
            self.judgement.setText('很遗憾！回答错误！')
            self.show_sys_A.setText('正确答案')
            text = ''
            for i in self.answerPool:
                text += i + '\n'
            self.sys_A.setText(text)
        self.Again.setEnabled(True)
        self.begin_yourQA.disconnect()   
    
    def play_Sys(self):
        self.no_Input.setChecked(False)
        self.no_Input.setEnabled(False)
        self.level_1.setEnabled(True)
        self.level_2.setEnabled(True)
        self.level_3.setEnabled(True)
        self.level_1.clicked.connect(self.choose_L1)
        self.level_2.clicked.connect(self.choose_L2)
        self.level_3.clicked.connect(self.choose_L3)
        self.is_Input.setEnabled(False)
        self.is_choose.setEnabled(False)
        self.Again.setEnabled(False)

    def choose_L1(self):
        self.level_1.setChecked(False)
        self.level_1.setEnabled(False)
        self.level_2.setEnabled(False)
        self.level_3.setEnabled(False)
        Match1 = match1.Match()
        Match1.make_M()
        eqt = None
        while True:
            eqt = Match1.make_Equation(20)
            if eqt is not None:
                break
        self.sysQ = Match1.get_Str(eqt)
        self.show_Q.setText('问题为')
        self.Q.setText(self.sysQ)
        self.answerPool = Match1.solve(self.sysQ)
        self.input_QA.setText('请输入答案')
        self.inputing_QA.setEnabled(True)
        self.begin_yourQA.setEnabled(True)
        self.level_1.disconnect()
        self.begin_yourQA.clicked.connect(self.Sys_A)

    def choose_L2(self):
        self.level_2.setChecked(False)
        self.level_2.setEnabled(False)
        self.level_1.setEnabled(False)
        self.level_3.setEnabled(False)
        Match2 = match1.Match()
        Match2.make_M()
        eqt = None
        while True:
            eqt = Match2.make_Equation(30)
            if eqt is not None:
                break
        self.sysQ = Match2.get_Str(eqt)
        self.show_Q.setText('问题为')
        self.Q.setText(self.sysQ)
        self.answerPool = Match2.solve(self.sysQ)
        self.input_QA.setText('请输入答案')
        self.inputing_QA.setEnabled(True)
        self.begin_yourQA.setEnabled(True)
        self.level_2.disconnect()
        self.begin_yourQA.clicked.connect(self.Sys_A)

    def choose_L3(self):
        self.level_3.setChecked(False)
        self.level_3.setEnabled(False)
        self.level_2.setEnabled(False)
        self.level_1.setEnabled(False)
        Match3 = match1.Match()
        Match3.make_M()
        eqt = None
        while True:
            eqt = Match3.make_Equation(40)
            if eqt is not None:
                break
        self.sysQ = Match3.get_Str(eqt)
        self.show_Q.setText('问题为')
        self.Q.setText(self.sysQ)
        self.answerPool = Match3.solve(self.sysQ)
        self.input_QA.setText('请输入答案')
        self.inputing_QA.setEnabled(True)
        self.begin_yourQA.setEnabled(True)
        self.level_3.disconnect()
        self.begin_yourQA.clicked.connect(self.Sys_A)

    def Sys_A(self):
        self.begin_yourQA.setChecked(False)
        self.begin_yourQA.setEnabled(False)
        self.show_your_A.setText('你的答案为')
        self.your_A.setText(self.inputing_QA.text())
        self.yourA = str(self.inputing_QA.text())
        self.inputing_QA.clear()
        self.input_QA.clear()
        self.inputing_QA.setEnabled(False)
        if self.yourA in self.answerPool:
            self.judgement.setText('恭喜你！回答正确！')
            self.show_sys_A.setText('其他答案')
            text1 = ''
            for i in self.answerPool:
                if i != self.yourA:
                    text1 += i + '\n'
            self.sys_A.setText(text1)
        else:
            self.judgement.setText('很遗憾！回答错误！')
            self.show_sys_A.setText('正确答案')
            text = ''
            for i in self.answerPool:
                text += i + '\n'
            self.sys_A.setText(text)
        self.Again.setEnabled(True)
        self.begin_yourQA.disconnect()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())