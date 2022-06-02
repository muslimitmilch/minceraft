import os, math, time

class advancedDisplay():

    def __init__(self):
        self.outputList = []
        self.homeListFinal = ['', '', '']
        self.logo = True
        self.longSpacer = '                                                                                                                                                                                  '
    
    def clear(self):
        self.outputList = []
        self.homeList = []
        os.system('clear')
        
    def listSet(self, appendObject):
        if(type(appendObject) is str):
            self.outputList = [appendObject]
        else:
            self.outputList = appendObject
        self.output()
        
    def listAppend(self, appendObject):
        if(type(appendObject) is str):
            self.outputList += [appendObject]
        else:
            self.outputList += appendObject
        self.output()
    
    def listAppendTop(self, appendObject):
        self.outputList.reverse()
        if(type(appendObject) is str):
            self.outputList += [appendObject]
        else:
            self.outputList += appendObject
        self.outputList.reverse()
        self.output()
        
    
    def homeSet(self, homeObject, homeLength = 5):
        self.homeList = []
        if(type(homeObject) is str):
            self.homeList += [homeObject]
        else:
            self.homeList += homeObject
        spacer = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        self.homeListFinal = [''] + spacer[:homeLength - 1] + self.homeList + ['']
        self.output()

    def output(self):
        terminalWidth, terminalLength = os.get_terminal_size(0)  
        logoLines = ["    __  ____                            ______ ",
"   /  |/  (_)___  ________  _________ _/ __/ /_",
"  / /|_/ / / __ \/ ___/ _ \/ ___/ __ `/ /_/ __/",
" / /  / / / / / / /__/  __/ /  / /_/ / __/ /_  ",
"/_/  /_/_/_/ /_/\___/\___/_/   \____/_/  \__/  "]
        os.system('clear')
        if(terminalLength > (len(self.homeListFinal) + len(self.outputList) + len(logoLines) + (terminalLength / 2))):
            for i in range(math.ceil(terminalLength/2) - len(logoLines) - 1):
                print()
            spacer = self.longSpacer[:math.floor((terminalWidth - 48) / 2)]
            for i in logoLines:
                print(spacer, i)
            for i in range(math.floor(terminalLength / 2) - len(self.outputList) - len(self.homeListFinal)):
                print()
        else:
            for i in range(terminalLength - len(self.homeListFinal) - len(self.outputList) - 1):
                print()
        for i in self.outputList:
            print('    ' + i)
        for i in self.homeListFinal:
            print('    ' + i)
            
    def userInput(self):
        return input('      ')
