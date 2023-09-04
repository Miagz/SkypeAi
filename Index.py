from SkShell import Ai_shell
from SkWeb import Ai_web
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SkypeAi')
    parser.add_argument('--shell',dest="shell",action='store_true',help='shell')
    parser.add_argument('--web',action='store_true',help='web')
    parser.add_argument('-p','--port',type=int,default=7777,help='port')

    args = parser.parse_args()
    strs = """
 ______   __                                     _        _   
.' ____ \ [  |  _                                / \      (_)  
| (___ \_| | | / ]   _   __  _ .--.   .---.     / _ \     __   
 _.____`.  | '' <   [ \ [  ][ '/'`\ \/ /__\\\\   / ___ \   [  | 
| \____) | | |`\ \   \ '/ /  | \__/ || \__., _/ /   \ \_  | |  
 \______.'[__|  \_][\_:  /   | ;.__/  '.__.'|____| |____|[___] 
                    \__.'   [__|                               
    """
    print(strs)
    if args.shell:  
        skype = Ai_shell()
        skype.get_info()
        skype.Skype_shell()
    elif args.web:
        skype = Ai_web()
        skype.Skype_web(args.port)