#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import psutil
import socket
#############################################
#  CPU:cpu核心数，CPU使用率
#  内存：总内存，已使用，空闲，使用率
#  磁盘：总空间，已使用，空间，使用率 （分目录)
#  IO: 磁盘、网络
#############################################
def gethostname():
    #import platform
    #platform.node()
    return socket.gethostname() 

def getip():
    ## IP可能不太准，只能手工去配置了！！
    #import platform
    #platform.node()
    try:
        ip = socket.gethostbyname(gethostname()) 
    except:
        ip='unknow'

    return ip 

class infoCollector:
    def __init__(self, saver=None):
        self.hostname = gethostname()
        self.ip = getip()

        if saver == None:
            self.saver = InfoSaver()
        else:
            self.saver = saver

    def __send_cpuinfo(self):
        # 逻辑CPU数量
        #cpu_count = psutil.cpu_count()
        #psutil.pids() #进程数
        #cpu = psutil.cpu_percent(percpu=True)
        #print(cpu)
        ci = psutil.cpu_times()
        # cpuinfo = {'hostname': self.hostname,
        #             'ip': self.ip,
        #             'ts': time.strftime("%Y%m%d%H%M%S", time.localtime()),
        #             'store_total': ci.user,
        #             'store_free': ci.system,
        #             'store_used': ci.idle,
        #             'percent': vm.percent }
        self.saver.save_cpuinfo(ci)

    def __send_meminfo(self):
        # 物理内存
        vm = psutil.virtual_memory()
        meminfo = {'hostname': self.hostname,
                    'ip': self.ip,
                    'ts': time.strftime("%Y%m%d%H%M%S", time.localtime()),
                    'metrics':{
                    'memory.total': vm.total,
                    'memory.free': vm.available,
                    'memory.used': vm.used,
                    'memory.percent': vm.percent }
                }
        self.saver.save_metric(meminfo)

        # 交换分区
        # swap = psutil.swap_memory()
        # print(swap)
    def __send_diskinfo(self):
        # 磁盘分区信息
        # NOTE:如果你只想获取某些指定文件系统的大小，可以在这里写死
        for i in psutil.disk_partitions():
            #print(i)
            # 磁盘使用情况
            disk = psutil.disk_usage(i.mountpoint)
            diskinfo = {'hostname': self.hostname,
                        'ip': self.ip,
                        'ts': time.strftime("%Y%m%d%H%M%S", time.localtime()),
                        'metrics':{},
                        'store_mountpoint': i.mountpoint,
                        'store_total': disk.total,
                        'store_free': disk.free,
                        'store_used': disk.used,
                        'percent': disk.percent}
            self.saver.save_diskinfo(diskinfo)

        # 磁盘IO
        # dio=psutil.disk_io_counters()
        # print(dio)

    def __send_networkinfo(self):
        # 网络信息
        nio = psutil.net_io_counters(pernic=True)
        self.saver.save_networkinfo(nio)

    def send(self):
        self.__send_cpuinfo()
        self.__send_meminfo()
        self.__send_diskinfo()
        #self.__send_networkinfo()
        self.saver.close()

class InfoSaver:
    """ 用来实现将监控数据写到数据库、MQ、ES、文件系统、HTTP Rest等位置,默认只是打印"""

    def __init__(self):
        pass

    def save_cpuinfo(self, cpuinfo):
        print(cpuinfo)

    def save_meminfo(self, meminfo):
        print(meminfo)

    def save_diskinfo(self, diskinfo):
        print(diskinfo)

    def save_networkinfo(self, networkinfo):
        print(networkinfo)
    def save_metric(self,metrics):
        pass
    def close(self):
        pass



if __name__ == "__main__":
    # saver = InfoSaver()
    from infoMySqlSaver import InfoMySqlSaver
    saver = InfoMySqlSaver()
    spider = infoCollector(saver)
    spider.send()


# print("-----------cpu_count-----------")
# print(psutil.cpu_count())  # 返回系统中逻辑cpu的数量
# print("-----------cpu_freq-----------")
# print(psutil.cpu_freq())  # 返回CPU频率
# print("-----------cpu_percent-----------")
# print(psutil.cpu_percent())  # 返回当前系统CPU利用率(float类型)
# print("-----------cpu_stats-----------")
# print(psutil.cpu_stats())  # 返回CPU统计数据
# print("-----------cpu_times-----------")
# print(psutil.cpu_times())  # 返回系统范围内的CPU时间。
# print("-----------cpu_times_percent-----------")
# print(psutil.cpu_times_percent())  # 对于每个特定的CPU时间提供利用率，由cpu_times()返回。
# print("-----------boot_time-----------")
# print(psutil.boot_time())  # 返回从1970以来以秒表示的系统启动时间
# print("-----------users-----------")
# print(psutil.users())  # 返回当前连接在系统上的用户列表

# print("-----------test-----------")
# print(psutil.test())  # 列出所有当前正在运行的进程信息
