#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
from info_spider import InfoSaver

class InfoMySqlSaver(InfoSaver):
    def __init__(self):
        self.db = pymysql.connect("10.10.10.100", "root", "admin", "test")

    def save_cpuinfo(self, cpuinfo):
        print(cpuinfo)

    def save_meminfo(self, meminfo):
        self.save_diskinfo(meminfo)

    def save_diskinfo(self, storageinfo):
        print("save storageinfo" + str(storageinfo))
        print(storageinfo.keys())
        try:
            with self.db.cursor() as cursor:
                cursor.execute("insert into smonitor_storage_info values('%s','%s','%s','%s','%s',%s,%s,%s,%s)"  % (storageinfo['hostname'],
                            storageinfo['ip'],
                            storageinfo['ts'],
                            storageinfo['store_device'].replace("\\","/"),
                            storageinfo['store_mountpoint'].replace("\\","/"),
                            storageinfo['store_total'],
                            storageinfo['store_free'],
                            storageinfo['store_used'],
                            storageinfo['percent']))
            self.db.commit()
        finally:
            self.db.close()

    def save_networkinfo(self, networkinfo):
        print(networkinfo)

    def close(self):
        self.db.close()