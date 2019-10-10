import random

#operation for one number
#Dec means moving away a matchstick
#Inc means adding a matchstick
#Selfchange means changing inside the number
class Action_type:
    Dec = 0
    Inc = 1
    Selfchange = 2

#position information of all elements
#Capital means the first element
#Default means other elements 
class Position_type:
    Default = 0
    Capital = 1

#Left/Right means on the left/right side of '='
class Side:
    Left = 0
    Right = 1

#some features of every element(+-*=0123456789) in the equation
#positiontypes: capital/default
#side: left/right
class Feature:
    def __init__(self, value, positiontype, side):
        self.value = value
        self.positiontype = positiontype
        self.side = side

class Match:

    def __init__(self):

        self.BCD = {
            0: [1, 1, 1, 1, 1, 1, 0],
            1: [0, 1, 1, 0, 0, 0, 0],
            2: [1, 1, 0, 1, 1, 0, 1],
            3: [1, 1, 1, 1, 0, 0, 1],
            4: [0, 1, 1, 0, 0, 1, 1],
            5: [1, 0, 1, 1, 0, 1, 1],
            6: [1, 0, 1, 1, 1, 1, 1],
            7: [1, 1, 1, 0, 0, 0, 0],
            8: [1, 1, 1, 1, 1, 1, 1],
            9: [1, 1, 1, 1, 0, 1, 1]
        }

        #used to save what the elements will change into after all kinds of operations
        self.M = {}
    
    
    '''used to find out which number the original one will change into after
    getting an extra matchstick from another element or giving one away'''
    def after_Moving(self, d, edge, actiontype):
        g = self.BCD[d].copy()
        if actiontype == Action_type.Inc:
            if g[edge] == 1:
                return None
            g[edge] = 1
            for i in range(10):
                if g == self.BCD[i]:
                    return i
        elif actiontype == Action_type.Dec:
            if g[edge] == 0:
                return None
            g[edge] = 0
            for i in range(10):
                if g == self.BCD[i]:
                    return i
    
    '''used to find out which number the original one will change into after
     changing the position of the composing matchsticks'''
    def after_Selfchanging(self, d):
        res = []
        for i in range(7):
            for j in range(i+1, 7):
                g = self.BCD[d].copy()
                if g[i] != g[j]:
                    t = g[i]
                    g[i] = g[j]
                    g[j] = t
                    for k in range(10):
                        if g == self.BCD[k] and d != k:
                            res.append(k)
        return res


    #used to save what the elements will change into after all kinds of operations
    def make_M(self):
        #plus sign won't occupy capital position
        self.M['+'] = {
            Action_type.Inc:{
                Position_type.Default:[]
            },
            Action_type.Dec:{
                Position_type.Default:['-']
            },
            Action_type.Selfchange:{
                Position_type.Default:[]
            }
        }
        #minus sign might occupy capital position
        self.M['-'] = {
            Action_type.Inc:{
                Position_type.Default:['+']
            },
            Action_type.Dec:{
                Position_type.Default:[],
                Position_type.Capital:['']
            },
            Action_type.Selfchange:{
                Position_type.Default:[]
            }
        }
        #times sign won't occupy capital position
        #it won't turn into any other element
        self.M['*'] = {
            Action_type.Inc:{
                Position_type.Default:[]
            },
            Action_type.Dec:{
                Position_type.Default:[],
            },
            Action_type.Selfchange:{
                Position_type.Default:[]
            }
        }
        
        #numbers
        for i in range(10):
            self.M[i] = {
                Action_type.Inc:{
                #they might occupy capital position
                #might turn into negatives
                Position_type.Capital:[-i],
                Position_type.Default:[]
            },
            Action_type.Dec:{
                Position_type.Default:[],
            },
            Action_type.Selfchange:{
                Position_type.Default:[]
            }  
            }
            for j in range(7):
                k = self.after_Moving(i, j, Action_type.Inc)
                if k is not None:
                    self.M[i][Action_type.Inc][Position_type.Default].append(k)
                k = self.after_Moving(i, j, Action_type.Dec)
                if k is not None:
                    self.M[i][Action_type.Dec][Position_type.Default].append(k)
                self.M[i][Action_type.Selfchange][Position_type.Default] = self.after_Selfchanging(i)
    
    #used to get the corresponding contents of a certain element
    def get_M(self, elm):
        if elm == '+' or elm == '-' or elm =='*':
            return self.M[elm]
        d = ord(elm) - ord('0')
        if 0 <= d <= 9:
            return self.M[d]

    #used to get every element's features   
    def get_Feature(self, eqtStr):
        eqt = []
        #whether '=' has been found 
        is_Eq = False
        #whether it is the beginning of the equation 
        is_Capital = True
        for s in eqtStr:
            if is_Capital:
                eqt.append(Feature(s, Position_type.Capital, Side.Left))
                is_Capital = False
                continue
            if s == '=':
                is_Eq = True
                continue
            if is_Eq:
                eqt.append(Feature(s, Position_type.Default, Side.Right))
            else:
                eqt.append(Feature(s, Position_type.Default, Side.Left))
        return eqt

    #used to check whether the equation is correct
    def is_Equal(self, eqt):
        is_Eq = False
        expleft = ''
        expright = ''
        for elm in eqt:
            if elm.side == Side.Left:
                expleft += str(elm.value)
            elif elm.side == Side.Right:
                expright += str(elm.value)
        i = 0
        while i < len(expleft) - 1:
            if expleft[i] == '0' and expleft[i+1].isdigit():
                expleft = expleft[:i] + expleft[i+1:]
            else:
                i += 1
        j = 0
        while j < len(expright) - 1:
            if expright[j] == '0' and expright[j+1].isdigit():
                expright = expright[:j] + expright[j+1:]
            else:
                j += 1
        if expleft == '' or expright == '':
            return 0
        elif eval(expleft) == eval(expright):
            return True
        else:
            return False
        
    #used to get string form of an equation
    def get_Str(self, eqt):
        s = ''
        is_Eq = False
        for elm in eqt:
            if not is_Eq and elm.side == Side.Right:
                is_Eq = True
                s += '='
            s += str(elm.value)
        return s

    #Used to remove unecessary zeros like the zero in 01
    # def remove_Zero(self, eqt, i):
    #     if eqt[i].value == 0:
    #         if i < len(eqt) - 1 and str(eqt[i + 1].value).isdigit() and eqt[i].side == eqt[i + 1].side:
    #             eqt.remove(eqt[i])
    #             return 1


    #core moving part
    def move_Match1(self, eqt):
        res = []
        for (i, elm) in enumerate(eqt):
            m = self.get_M(elm.value)
            #SelfChange
            for t in m[Action_type.Selfchange][Position_type.Default]:
                newEqt = eqt.copy()
                newEqt[i] = Feature(t, elm.positiontype, elm.side)
                # self.remove_Zero(newEqt, i)
                res.append(newEqt)

            #Move
            t0List = m[Action_type.Dec][Position_type.Default]
            if elm.positiontype == Position_type.Capital and Position_type.Capital in m[Action_type.Dec]:
                t0List.extend(m[Action_type.Dec][Position_type.Capital])
            for t0 in t0List:
                newEqt0 = eqt.copy()
                newEqt0[i] = Feature(t0, elm.positiontype, elm.side)
                # debug
                # self.remove_Zero(newEqt0, i)
                for (i1, elm1) in enumerate(newEqt0):
                    # debug
                    if i == i1:
                        continue
                    m1 = self.get_M(elm1.value)
                    t1List = m1[Action_type.Inc][Position_type.Default]
                    if elm1.positiontype == Position_type.Capital and Position_type.Capital in m1[Action_type.Inc]:
                        t1List.extend(m1[Action_type.Inc][Position_type.Capital])
                    for t1 in t1List:
                        newEqt1 = newEqt0.copy()
                        newEqt1[i1] = Feature(t1, elm1.positiontype, elm1.side)
                        # flag = self.remove_Zero(newEqt1, i1)
                        # if i1 < i and flag == 1:
                        #     self.remove_Zero(newEqt1, i - 1)
                        # else:
                        #     self.remove_Zero(newEqt1, i)
                        res.append(newEqt1)
        return res

    #core judging part
    def solve(self, eqtStr):
        answerpool = set()
        eqt = self.get_Feature(eqtStr)
        res = self.move_Match1(eqt)
        for newEqt in res:
            if self.is_Equal(newEqt):
                    answerpool.add(self.get_Str(newEqt))
        return answerpool

    #if the player is not going to input
    #make an equation(correct/wrong) to play
    #maxNum means the possible maximum of the numbers at the left side
    def make_Equation(self, maxNum):
        eqtStr = str(random.randint(maxNum - 30,maxNum))
        if random.random() < 0.45:
            eqtStr += '+'
        elif 0.45 <= random.random() < 0.9:
            eqtStr += '-'
        else:
            eqtStr += '*'
        eqtStr += str(random.randint(maxNum - 30,maxNum))
        r = eval(eqtStr)
        eqtStr += '=' + str(r)
        eqt = self.get_Feature(eqtStr)
        res = self.move_Match1(eqt)
        if len(res) == 0:
            return None
        questionpool = []
        for newEqt in res:
            if not self.is_Equal(newEqt):
                questionpool.append(newEqt)
        if len(questionpool) == 0:
            return None
        return questionpool[random.randint(0,len(questionpool) - 1)]

    
    #the player can choose to input an equation(correct/wrong)
    #if there is no input, make one
    #change the degree of difficulty by changing maxNum
    #debug
    def start_Gaming(self):
        is_Input = input('Would you like to make a question by yourself?')
        if is_Input == 'y' or is_Input =='Y':
            question = input('Then the question is:')
            q = self.get_Feature(question)
            if self.is_Equal(q):
                print('Already correct!')
            else:
                answerPool = self.solve(question)
                if len(answerPool) == 0:
                    print('No answer!')
                else:
                    answer = input('Your answer:')
                    if answer in answerPool:
                        print('Correct! Other answer(s):')
                        for i in answerPool:
                            if i != answer:
                                print(i)
                    else:
                        print('Wrong! The correct answer(s):')
                        for j in answerPool:
                            print(j)
        
        elif is_Input == 'n' or is_Input =='N':
            #choice of the degree of difficulty
            level = input('Level:')
            if level == '1':
                maxNum = 30
            elif level == '2':
                maxNum = random.randint(31, 60)
            elif level == '3':
                maxNum = random.randint(61, 90)
            while True:
                eqt = self.make_Equation(maxNum)
                if eqt is not None:
                    break
            question = self.get_Str(eqt)
            print('Then the question is: %s'%question)
            answer = input('Your answer:')
            answerPool = self.solve(question)
            if answer in answerPool:
                print('Correct! Other answer(s):')
                for i in answerPool:
                    if i != answer:
                        print(i)
            else:
                print('Wrong! The correct answer(s):')
                for j in answerPool:
                    print(j)
    
    def preTest(self, question):
        q = self.get_Feature(question)
        #if the equation is already correct
        if self.is_Equal(q) == True:
            return 1
        elif self.is_Equal(q) == False:
            answerPool = self.solve(question)
            #if there is no answer
            if len(answerPool) == 0:
                return 2
            else:
                return answerPool
        #if the input is illegal
        else:
            return 0





if __name__ == "__main__":
    match = Match()
    match.make_M()
    match.start_Gaming()