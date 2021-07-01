# define dataset class to feed the model
import numpy as np 
import os
import sys
import time

class ProgressBar():
    def __init__(self,worksum,info="",auto_display=True):
        self.worksum = worksum
        self.info = info
        self.finishsum = 0
        self.auto_display = auto_display
    def startjob(self):
        self.begin_time = time.time()
    def complete(self,num):
        self.gaptime = time.time() - self.begin_time
        self.finishsum += num
        if self.auto_display == True:
            self.display_progress_bar()
    def display_progress_bar(self):
        percent = self.finishsum * 100 / self.worksum
        eta_time = self.gaptime * 100 / (percent + 0.001) - self.gaptime
        strprogress = "[" + "=" * int(percent // 2) + ">" + "-" * int(50 - percent // 2) + "]"
        str_log = ("%s %.2f %% %s %s/%s \t used:%ds eta:%d s" % (self.info,percent,strprogress,self.finishsum,self.worksum,self.gaptime,eta_time))
        sys.stdout.write('\r' + str_log)
