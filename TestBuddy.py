import os
import random

def AnswerQuestions(fname):    
    with open(fname) as f:
        content = f.readlines()
        random.shuffle(content)
        wrong = 0
        totalquestions = 0
        wrongarr = list()
        for q in content:
            print (q.partition('::')[0])
            
            myanswer = raw_input('->  ')
            theanswer = q.partition('::')[2]  
            if myanswer == 'finish':
                FinishNow(wrong, totalquestions, wrongarr)
            else:
                totalquestions = totalquestions + 1
            if myanswer == theanswer.strip():
                print("correct")
            else:
                print("wrong, you said:" + myanswer + "   answer is:" + theanswer.strip())
                wrongarr.append(q)
                wrong = wrong + 1
    FinishNow(wrong, totalquestions, wrongarr)
        
def FinishNow(wrong, totalquestions, wrongarr):
    if totalquestions != 0:
        if wrong != 0:
            print(" here are the mistakes: ")
            for e in wrongarr:
                print(e)        
        elif wrong == 0:
            print("100% correct")
        print("you got " + str(wrong) + " incorrect answers of " + str(totalquestions) + " questions answered.")
        print("that's " +  str(float(float(totalquestions - wrong) / float(totalquestions)) * 100) + "% correct"  )
    exit()
    
def Main():
    print(":: TestBuddy by Daryl Petty, dazpetty.com, Creative Commons, CC0, no rights reserved ::")
    print(":: TestBuddy by DazPetty.com ::")
    tfname = raw_input("practice test to open:")
    print(":: type 'finish' to end test ::")
    AnswerQuestions(tfname)

if __name__ == '__main__':
    Main()