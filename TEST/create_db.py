#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2020-8-9 23:11:00
# version: 1.0
# __author__: zhilong
import pymysql
def main():
    conn = pymysql.connect(host='localhost', user='root', password='rootpwd', db='novelsite')
    cursor = conn.cursor()
    sql = 'create table novel(novelid int primary key auto_increment,' \
          'type int not null ,' \
          'sort varchar(100),' \
          'novelname varchar(100),' \
          'novelimg varchar(200),' \
          'description text,' \
          'state varchar(40),' \
          'author varchar(40) )'
    sql3 = 'create table charpter(charpterid int primary key auto_increment,' \
           'novelid int,' \
           'foreign key (novelid) references novel(novelid),' \
           'title varchar(100),' \
           'content text,' \
           'sid int )'
    cursor.execute(sql3)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()





