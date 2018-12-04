import time
import subprocess
from info_spider import infoCollector

class SCInfoCollector(infoCollector):
    """ 收集大数据平台各租户资源使用情况 """
    def __init__(self,queue_name,only_yarn=False,saver=None):
        super().__init__(saver)
        self.queue_name = queue_name
        self.only_yarn = only_yarn

    def __send_yarn(self):
        #output = subprocess.getoutput(""" yarn queue -status %s|egrep -i "capacity|state" | awk -F":" '{print $2}' """ % self.queue_name)
        output='RUNNING\n 8.4%\n 98%\n 8.4%'
        if output == None or len(output.split("\n")) != 4:
            yarninfo = {}
        else:
            y = output.split("\n")
            yarninfo = {
                'hostname': self.hostname,
                'ip': self.ip,
                'ts': time.strftime("%Y%m%d%H%M%S", time.localtime()),
                'metrics': {
                    'yarn.c1.'+self.queue_name+'.state': y[0],
                    'yarn.c1.'+self.queue_name+'.capacity': y[1],
                    'yarn.c1.'+self.queue_name+'.current_capacity': y[2],
                    'yarn.c1.'+self.queue_name+'.max_capacity': y[3]
                }
            }
        self.saver.save_metric(yarninfo)

    def send(self):
        if not self.only_yarn:
            super().send()
        self.__send_yarn()
