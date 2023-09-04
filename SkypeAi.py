from pyquery import PyQuery as pq
from reprint import output
from skpy import Skype,SkypeNewMessageEvent,SkypeEditMessageEvent,SkypeChats
import readline
from bs4 import BeautifulSoup
import yaml


class Skype_AI(object):
    global_session = "" 
    session_list = []
    session_dict = {}
    schema = "平衡模式"
    """
    global_session 用于对接session会话,修改可更改用户会话
    session_list 获取用户可对话列表 列表类型: SkypeGroupChat
    session_dict 获取用户 会话名以及会话id 键值对
    """
    def __init__(self):
        with open('config.yaml',encoding='utf-8') as file1:
            self.dict = yaml.load(file1,Loader=yaml.FullLoader)

        self.UserMail = self.dict['mail']
        self.UserPass = self.dict['password']
        self.loggedInUser = Skype(self.UserMail,self.UserPass)
        self.session = ""
    def send_message(self,prompet):
        self.loggedInUser.conn
        """
        发送信息
        """
        self.SendMsgTo=self.loggedInUser.chats[Skype_AI.global_session]
        self.SendMsgTo.sendMsg("<at id=\"28:cf0e6215-34fe-409b-9e4b-135d7f3aa13b\">Bing</at> {}".format(prompet),rich=True)
    """
    监控最新信息以及 修改后的信息
    """
    def get_message(self):
        Miagz = True
        with output(output_type='list') as output_lines:
            while Miagz:
                events = self.loggedInUser.getEvents()
                for event in events: 
                    if isinstance(event, SkypeNewMessageEvent): #新消息监听
                        html = event.msg.content
                        data = str(pq(str(html)))
                        text = data.replace("<br/>","\n").replace("<br />","\n")
                        soup = BeautifulSoup(text, 'html.parser')
                        oktext = soup.find("bing-response").text.strip().replace("blush","").replace("smile","").replace("wink","").replace("grin","").replace("感谢您使用必应搜索引擎。","").replace("我是必应,","").replace("感谢您继续使用必应搜索引擎。","").replace("• Bing: ","").replace("这是Bing。","")
                        output_lines[0] = "SkypeAi: "+oktext
                        if oktext[-3:]!="...":
                            Miagz=False
                            return oktext
                    if isinstance(event, SkypeEditMessageEvent): # 检查是否是消息修改事件
                        html = event.msg.content
                        data = str(pq(str(html)))
                        text = data.replace("<br/>","\n").replace("<br />","\n")
                        soup = BeautifulSoup(text, 'html.parser')
                        oktext = soup.find("bing-response").text.strip().replace("blush","").replace("smile","").replace("wink","").replace("grin","").replace("感谢您使用必应搜索引擎。","").replace("我是必应,","").replace("感谢您继续使用必应搜索引擎。","").replace("• Bing: ","").replace("这是Bing。","")
                        output_lines[0]="SkypeAi: "+oktext
                        if oktext[-3:]!="...":
                            Miagz=False
                            return oktext
    """
    创建新会话
    session_name 会话名
    """
    def create_session(self,session_name):
        session  = self.loggedInUser.chats.create([])
        session.setTopic =  session_name
        session.addMember("cf0e6215-34fe-409b-9e4b-135d7f3aa13b")
        return "会话"+session_name+"创建成功！"
    
    """
    删除当前会话
    """
    def remove_session(self):
        self.loggedInUser.removeMember(self.loggedInUser.userId)
        return "当前会话删除成功！"
    

    """
    获取session list
    """
    def get_session_list(self):
        session_list = []
        get_group_info = SkypeChats(self.loggedInUser).recent()

        for lists in get_group_info.keys():
            try:
                if len(get_group_info[lists].userIds)==2:
                    session_list.append(get_group_info[lists])
                    Skype_AI.session_dict[get_group_info[lists].topic] = lists
            except AttributeError:
                continue
        return session_list
    

  