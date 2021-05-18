#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2020-8-9 23:11:00
# version: 1.0
# __author__: zhilong
from bs4 import BeautifulSoup
html = BeautifulSoup(open('aaa.html'), 'html.parser')
html.prettify()
# li_lists = html.search('.section.board-list.board-list-collapse ul li')
li_lists = html.search('.section .board-list .board-list-collapse ul li')

# section[@class="section board-list board-list-collapse"]/ul/li
for li in li_lists:
    # ./a/img/@src
    src = li.search('a img').src
    print(src)



