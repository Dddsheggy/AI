人工智能基础第一次大作业（first文件夹）：火柴等式

主要功能：移动一根火柴棍使等式成立，问题等式给出的形式可以为：①题库中选择题目 ②玩家自己输入题目 ③系统自动生成题目

①题库中选择题目：初级‘3+3=0’，中级‘6+4=4’，高级‘45+46=99’

②玩家自己输入题目：有检查输入模块，针对①输入不合法（如输入‘5+3’） ②输入的题目已经是等式 ③输入的题目无解 三种情况给出不同的错误提示

③系统自动生成题目：初中高级操作数的范围有所不同，具体参见match1.py中make_Equation函数和show_main.py中choose_L1,choose_L2和choose_L1函数

玩家输入自己的答案后可判断此输入是否正确，若不正确则给出错误提示及正确答案，否则给出正确提示和其他可能答案
