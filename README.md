## SkypeAi简介
SkypeAi能在大陆无需魔法(VPN)即可访问微软NewBing服务。无需使用VPN即可接入NewBing到微信或者QQ等聊天软件，实现聊天机器人功能！



### 安装
> git clone https://github.com/Miagz/SkypeAi.git
>
> python3 -m pip install -r requirements.txt
### 需求
- python3.8+
- 用于newBing测试资格
- 仅需微软账号密码即可使用

### 如何使用
SkypeAi拥有Web api模式以及终端命令行模式

在config.yaml输入微软账号和密码

##### Web api模式
web API模式 默认端口为7777
> python3 Index.py --web 

设置api端口
>python Index.py --web -p 7777

##### 终端命令行模式
启动命令行模式
>python3 Index.py --shell

命令行快捷启动
>echo "alias ai(设置的快捷方式名)='python3 your_file_path/Index.py --shell'" >> ~/.bashrc(zsh shell下写入到 ~/.zshrc)


###### 终端命令行模式-功能
- *会话模式*｜   会话模式分别为**平衡模式**、**创造模式**、**精确模式** 默认情况下为**平衡模式**，输入1、2、3分别切换至**平衡模式**、**创造模式**、**精确模式**，也可以直接输入需要的模式进行切换
  ![Alt text](https://github.com/Miagz/SkypeAi/blob/main/img/CleanShot%202023-09-04%20at%2017.16.07%402x.png)
  
- *会话列表*｜ 输入**会话列表** or **session list**可查看skype会话列表(只能查看前十行)

- 创建新会话｜ 输入**创建会话** or **new session**可创建新会话

- 切换会话｜ 输入**切换会话** or **use 会话名**可切换会话

- 删除会话 ｜ 输入**删除会话** or **delete session**可删除会话

- 退出会话 ｜ 输入**quit** or **by** or **exit**可退出会话

### Demo

![Alt text](https://github.com/Miagz/SkypeAi/blob/main/img/demo.gif)

#### 二次开发
1、使用SkypeAi 的web api模式，接入NewBing到微信或者QQ等聊天软件，实现聊天机器人功能
![Alt text](https://github.com/Miagz/SkypeAi/blob/main/img/CleanShot%202023-09-04%20at%2017.32.15%402x.png)
2、直接copy SkypeAi文件和skpy文件夹(skpy库我稍微修改了一下)到自己项目中接入NewBing,进行二次开发。
