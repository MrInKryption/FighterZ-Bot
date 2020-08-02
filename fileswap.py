##Written my MrInKryption
##Subject to free use without plagiarism


import os

def enter_dir(): 
    login = os.getlogin()
    
    dir_name='C:\\Users\\'+login+'\\AppData\\Local\\DBFighterZ\\Saved\\SaveGames\\'
    os.chdir(dir_name)
    dirs = os.listdir('.')
    os.chdir(dirs[0])
    #print(os.getcwd())
    foo = os.getcwd()
    return foo
    

def copy_file():
    

def main():
    print(enter_dir())

main()
