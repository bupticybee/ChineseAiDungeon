class Story():
    def __init__(self,background,title):
        self.background = background.replace("\n","")
        self.title = title.replace("\n","")
        self.story = []
    
    def add_action(self,action,action_type,result,summary):
        self.story.append([action.replace("\n",""),action_type.replace("\n",""),result.replace("\n",""),summary.replace("\n","")])
        
    def to_str(self):
        outstr = f"<start>\n故事名称：\n{self.title}\n故事背景：\n{self.background}"
        for one_action,one_action_type,one_result,one_summary in self.story:
            outstr += "\n" + "-" * 20
            outstr += f"\n动作：\n{one_action_type}\n{one_action}\n结果：\n{one_result}\n梗概：\n{one_summary}"
        outstr += "\n<end>"
        return outstr
    
    def to_dungeon_format(self):
        outstr = f"{self.background}"
        for one_action,one_action_type,one_result,one_summary in self.story:
            if one_action_type == "做":
                outstr += f"\n> 你{one_action}\n{one_result}"
            elif one_action_type == "说":
                outstr += f"\n> 你说“{one_action}”\n{one_result}"
        return outstr
    
    def to_normal_format(self):
        outstr = f"{self.background}"
        for one_action,one_action_type,one_result,one_summary in self.story:
            if one_action_type == "做":
                outstr += f"\n你{one_action}\n{one_result}"
            elif one_action_type == "说":
                outstr += f"\n你说“{one_action}”\n{one_result}"
        return outstr
    
    def from_file(self,fname):
        with open(fname,'r') as fhdl:
            self.load_content(fhdl)
        return self
    
    def load_content(self,content):
        self.story = []
        file_line = 0
        action = None
        action_type = None
        result = None
        summary = None
        for line in content:
            linesp = line.strip()
            if (file_line == 0):
                assert(linesp == "<start>")
            elif (file_line == 1):
                assert(linesp == "故事名称：")
            elif (file_line == 2):
                self.title = linesp
            elif (file_line == 3):
                assert(linesp == "故事背景：")
            elif (file_line == 4):
                self.background = linesp
            elif ((file_line - 5) % 8 == 0):
                if(linesp == "<end>"):
                    break
                assert(linesp == "--------------------")
            elif ((file_line - 5) % 8 == 1):
                assert(linesp == "动作：")
            elif ((file_line - 5) % 8 == 2):
                action_type = linesp
            elif ((file_line - 5) % 8 == 3):
                action = linesp
            elif ((file_line - 5) % 8 == 4):
                assert(linesp == "结果：")
            elif ((file_line - 5) % 8 == 5):
                result = linesp
            elif ((file_line - 5) % 8 == 6):
                assert(linesp == "梗概：")
            elif ((file_line - 5) % 8 == 7):
                summary = linesp
                self.add_action(action,action_type,result,summary)
            file_line += 1
            
class Stories():
    def __init__(self,fname):
        self.stories = []
        content = open(fname).read()
        while True:
            story = Story("","")
            p1 = content.find("<start>")
            if(p1 == -1):
                break
            p2 = content.find("\n<end>")
            one_content = content[p1:p2].split("\n")
            story.load_content(one_content)
            content = content[p2+6:]
            self.stories.append(story)
            
            