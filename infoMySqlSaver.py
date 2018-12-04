#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
from info_spider import InfoSaver


class InfoMySqlSaver(InfoSaver):
    def __init__(self,db_host="10.10.10.100",db_user="root",db_pwd="admin",db_name="test"):
        self.db = pymysql.connect(db_host, db_user, db_pwd, db_name)

    def save_metric(self, metrics):
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
            pass
            #self.close()

    def save_networkinfo(self, networkinfo):
        print(networkinfo)

    def close(self):
        self.db.close()
