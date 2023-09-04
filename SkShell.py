from SkypeAi import Skype_AI
class Ai_shell(Skype_AI):
    def __init__(self):
        super(Ai_shell, self).__init__()
    
    def Skype_shell(self):

        while True:
            prompet = input("\n{}~ >".format(Skype_AI.schema))
            if prompet == "exit" or prompet == "quit" or prompet=="by":
                break
            if prompet=="" or prompet==" " or prompet=="\n":
                continue
            ai = Skype_AI()
            if prompet == "1" or prompet =="平衡模式":
                ai.send_message("平衡模式")
                Skype_AI.schema = "平衡模式"
            elif prompet == "2" or prompet =="创造模式":
                ai.send_message("创造模式")
                Skype_AI.schema = "创造模式"
            elif prompet == "3" or prompet =="精确模式":
                ai.send_message("精确模式")
                Skype_AI.schema = "精确模式"
            elif prompet == "会话列表" or prompet =="session list":
                session = Skype_AI.session_list
                for i in session:
                    print(i.topic,end=" ")
                continue
            elif prompet[:3] == "切换 " or prompet[:4] == "use ":
                try:
                    Skype_AI.global_session = Skype_AI.session_dict[prompet[3:].strip()]
                    print("切换成功")
                    continue
                except KeyError:
                    print("会话不存在")
                    continue
            elif prompet == "删除会话" or prompet =="delete session":
                self.remove_session()
                continue
            elif prompet == "创建会话" or prompet =="new session":
                self.create_session()
                continue
            else:
                ai.send_message(prompet)

            ai.get_message()

    def create_session(self):
        session  = self.loggedInUser.chats.create([])
        question = input("请输入会话名(默认为session): ")
        print(question,type(question))
        if question == "" or question == " " or len(question)<=1:
            session.setTopic("session")
        session.setTopic(question)
        session.addMember("cf0e6215-34fe-409b-9e4b-135d7f3aa13b")
        print("会话"+question+"创建成功！")


    def remove_session(self):
        # 删除当前会话
        quesiont = input("是否删除当前会话? [y/n]: ")
        while True:
            if quesiont == "yes" or quesiont == "y" or quesiont == "YES" or quesiont == "Y":
                group_chats = self.loggedInUser.chats[Skype_AI.global_session]
                group_chats.removeMember(self.loggedInUser.userId)
                aws = "当前会话删除成功！"
                break
            elif quesiont == "no" or quesiont == "n" or quesiont == "NO" or quesiont == "N":
                aws = "以取消！"
                break
            else:
                continue
        
        print(aws)
        return aws

    def get_info(self):
        Skype_AI.session_list = self.get_session_list()
        if Skype_AI.session_list == []:
            while True:
                question = input("会话列表中并没有会话。是否创建新会话？[y/n]")
                if question == "y" or question == "Y" or question == "yes" or question == "Yes":
                    self.create_session()
                    aws = "会话创建成功！"
                    break
                elif question == "n" or question == "N" or question == "no" or question == "No":
                    aws = "Ok!"
                    break
                else:
                    continue
            print(aws)
        
        session = Skype_AI.session_list[0]
        Skype_AI.global_session = session.id
        session_info = """当前会话Id : {}\n当前会话名 : {}\n1:平衡模式 2:创造模式 3:精确模式""".format(session.id,session.topic)
        print(session_info)
        return session_info
    
