# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class QuanshuspiderPipeline:
    def process_item(self, item, spider):
        return item


class mysqlPipeline(object):
    def __init__(self):
        # self.ids_seen = set()
        self.db = pymysql.connect(
            host='localhost',  # 连接的是本地数据库
            user='root',  # 自己的mysql用户名
            passwd='rootpwd',  # 自己的密码
            db='novelsite',  # 数据库的名字
            charset='utf8mb4',  # 默认的编码方式：
            cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        '''
        :param item: 对象
        :param spider: 爬虫
        :return:
        '''
        # if item['sid'] in self.ids_seen:
        #     raise DropItem('Duplicate item found: %s' % item)
        # else:
        #     self.ids_seen.add(item['sid'])
        # 将爬取的信息保存到mysql
        # 将item里的数据拿出来
        # title = item['title']
        # link = item['link']
        # posttime = item['posttime']
        if spider.__class__.__name__ == 'Charpter01Spider':
            if item.__class__.__name__ =='QuanshuspiderItem':
                type = int(item["type"])
                sort = item["sort"]
                novelname = item["novelname"]
                novelimg = item["novelimg"]
                description = item["description"]
                state = item['state']
                author = item['author']

                # 和本地的newsDB数据库建立连接

                try:
                    # 使用cursor()方法获取操作游标
                    # cursor = self.db.cursor()
                    # SQL 插入语句

                    sql1 = 'select novelid from novel where novelname = ("%s")' % novelname
                    print(sql1)
                    self.cursor.execute(sql1)
                    data = self.cursor.fetchone()
                    if not data:

                        sql = "INSERT INTO novel(type,sort,novelname,novelimg,description ,state,author) \
                              VALUES (%d,'%s','%s','%s', '%s', '%s','%s')" % (type, sort, novelname, novelimg, description, state, author)
                        # 执行SQL语句
                        print('-----> sql语句是：', sql)
                        self.cursor.execute(sql)
                        # 提交修改
                        self.db.commit()
                except Exception as e:
                    print('-----> 存储数据出错了', e)
                    # 关闭连接
                    # self.db.rollback()
                    # self.cursor.close()
            else:
                # 向数据库表中写入数据
                # 来自于章节页
                try:
                    print('22222222222222222222222222222222')
                    print('-----> 想数据库章节表中写入数据。。。')
                    column = item['novelname'].split('《')[1].split('》')[0]
                    sql = 'select novelid from novel where novelname = ("%s") ' % column
                    print('第一条sql语句是', sql)
                    self.cursor.execute(sql)
                    novelid = self.cursor.fetchone()
                    print('novelid是：', novelid)
                    if novelid:
                        sql2 = 'insert into charpter(novelid,title,content,sid) values ("%s","%s","%s",%s)' % (novelid['novelid'], item['title'], item['content'],item['sid'])
                        # print('-----> 存储章节表的sql语句是：', sql2)
                        self.cursor.execute(sql2)
                        # 提交修改
                        self.db.commit()
                        print('写入ok!!!!!!!!!!!!!!!')
                except Exception as e:
                    print('存储表章节出错了！', e)
        else:
            try:
                print('-----> 想数据库章节表中写入数据。。。')
                sql = 'select novelid from novel where novelname = ("%s") ' % item['novelname']
                self.cursor.execute(sql)
                novelid = self.cursor.fetchone()
                if novelid:
                    sql2 = 'insert into charpter(novelid,title,content) values ("%s","%s","%s")' % (
                    novelid, item['title'], item['content'])
                    print('-----> 存储章节表的sql语句是：', sql2)
                    self.cursor.execute(sql2)
                    # 提交修改
                    self.db.commit()
            except Exception as e:
                print('存储表章节出错了！', e)

        return item

    def close_spider(self, spider):
        self.db.close()
