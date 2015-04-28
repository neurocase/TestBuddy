import os
import random
from colorama import Fore, Back, Style
from string import whitespace
import subprocess
from optparse import OptionParser



def formatStringForChecking(originalstring):
    formattedstring = originalstring.replace('\"','\'')
    formattedstring = formattedstring.replace(' ', '')
    formattedstring = formattedstring.strip() 
    return formattedstring

def AnswerQuestions(content):
    random.shuffle(content)
    debug = False
    wrong = 0
    totalquestions = 0
    wrongarr = list()
    for q in content:
        theanswer = q.partition(':ANSWER:')[2]
        if theanswer != "(note)":
            print (q.partition(':ANSWER:')[0])
            myanswer = raw_input(' ->  ')


            fmtmyanswer = formatStringForChecking(myanswer)
            fmttheanswer = formatStringForChecking(theanswer)
            #check the answer is not actually a command to finish or debug
            if myanswer == 'finish':
                FinishNow(wrong, totalquestions, wrongarr)
            elif myanswer == 'debug':
                debug = True
            else:
                # Assume is a valid attempt to answer the question
                totalquestions = totalquestions + 1
                if fmtmyanswer.strip() == fmttheanswer.strip():
                    print(Fore.YELLOW + "   " + theanswer.strip() + " is CORRECT" + Fore.RESET)
                else:
                    print(Back.RED + "   WRONG, you said:" + myanswer + "   answer is:" + theanswer.strip() + "   " + Back.RESET)
                    if debug == True:
                        print(Back.BLUE + fmtmyanswer + ":ANSWER:" + fmttheanswer + Back.RESET)
                    wrongarr.append(q)
                    wrong = wrong + 1
        else:
            print ("")
            print (Back.WHITE + "  " + Back.BLUE + Fore.WHITE + "  " + q.partition(':ANSWER:')[0]  + "    " + Back.WHITE + "   " + Back.RESET + Fore.RESET) 
            print ("")
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

    parser = OptionParser()
    parser.add_option("--dir", dest="currentdir", help="current directory to look for files")
    (options, args) = parser.parse_args()
    print options.currentdir
    print(Back.BLUE + "   " + ":: TestBuddy by Daryl Petty, dazpetty.com, Creative Commons, CC0, no rights reserved ::    " + Back.RESET)
    print(Fore.BLUE + "   " + ":: TestBuddy by DazPetty.com ::" + Fore.RESET)
    pwd = subprocess.call("pwd")
    print ("CURRENT DIRECTORY CONTAINS:")
    flist = os.listdir(options.currentdir)
    print flist
    tfname = raw_input("   practice test to open:")
    print("   " + ":: type 'finish' to end test ::")
    with open(tfname) as f:
        content = f.readlines()
        AnswerQuestions(content)

if __name__ == '__main__':
    Main()
