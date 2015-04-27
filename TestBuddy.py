import os
import random
from colorama import Fore, Back, Style




def AnswerQuestions(content):
    random.shuffle(content)
    wrong = 0
    totalquestions = 0
    wrongarr = list()
    for q in content:
        print (q.partition('::')[0])
        myanswer = raw_input(' ->  ')
        theanswer = q.partition('::')[2]
        nospacemyanswer = myanswer.replace(' ', '')
        nospacemyanswer = myanswer.replace('\"','\'')
        nospacetheanswer = theanswer.replace(' ', '')
        nospacetheanswer = theanswer.replace('\"','\'')
        #print(nospacemyanswer + "     " + nospacetheanswer)
        if myanswer == 'finish':
            FinishNow(wrong, totalquestions, wrongarr)
        else:
            totalquestions = totalquestions + 1

        if nospacemyanswer.strip() == nospacetheanswer.strip():
            print(Fore.YELLOW + "   " + theanswer.strip() + " is CORRECT" + Fore.RESET)
            #if myanswer == theanswer.strip():
            #   print("correct")
        else:
            print(Back.RED + "   WRONG, you said:" + myanswer + "   answer is:" + theanswer.strip() + "   " + Back.RESET)
            wrongarr.append(q)
            wrong = wrong + 1
    FinishNow(wrong, totalquestions, wrongarr)

def FinishNow(wrong, totalquestions, wrongarr):
    if totalquestions != 0:
        if wrong != 0:
            retry = raw_input("   " + " do you want to retry wrong answers? y/n: ")
            if retry == 'y':
                AnswerQuestions(wrongarr)
            print("   " + " here are the mistakes: ")
            for e in wrongarr:
                print(e)
        elif wrong == 0:
            print(Fore.GREEN + "   " + "100% correct" + Fore.RESET)
        print("   " + "you got " + str(wrong) + " incorrect answers of " + str(totalquestions) + " questions answered.")
        print("   " + "that's " +  str(float(float(totalquestions - wrong) / float(totalquestions)) * 100) + "% correct"  )
    exit()

def Main():
    print(Back.BLUE + "   " + ":: TestBuddy by Daryl Petty, dazpetty.com, Creative Commons, CC0, no rights reserved ::    " + Back.RESET)
    print(Fore.BLUE + "   " + ":: TestBuddy by DazPetty.com ::" + Fore.RESET)
    tfname = raw_input("   practice test to open:")
    print("   " + ":: type 'finish' to end test ::")
    with open(tfname) as f:
        content = f.readlines()
        AnswerQuestions(content)

if __name__ == '__main__':
    Main()