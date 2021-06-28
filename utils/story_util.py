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