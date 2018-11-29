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

    def save_diskinfo(self, metrics):
        # print("save storageinfo" + str(metrics))
        # print(metrics.keys())
        try:
            with self.db.cursor() as cursor:
                for k in metrics['metrics']:
                    #print(k+ ":" + str(metrics['metrics'][k]))
                    cursor.execute("insert into smonitor_metrics values('%s','%s','%s','%s','%s')" %
                                   (metrics['hostname'], metrics['ip'],
                                    metrics['ts'], k, metrics['metrics'][k])
                                   )

            self.db.commit()
        finally:
            self.db.close()

    def save_networkinfo(self, networkinfo):
        print(networkinfo)

    def close(self):
        self.db.close()
