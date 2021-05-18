# 创建个人网站基础操作（手把手教你从零开始用WordPress建站 (一步步建站, 一步也不少)）
### usdomain注册，域名，主机

1. 如何购买网站和ssl加密
```
    1.进入usdomaincenter.com网站，购买域名和想要的网站，
    2.不添加隐私保护，no thanks
    3.linux webhosting,选择cPanel Economy,添加到购物车，Add to Cart,
    4.购买ssl加密，点击顶部菜单Security，选择ssl，标准版ssl 1-site
    5.付款，检查购物车的内容
    6.选择优惠， Hava a promo code? 输入：100CR15
    7.创建账户,设置 email username password support pin）
    8.注册完账号，回到付款页面，填写billing information
    9.进入付款步骤，支持不同付款方式
```
2. 如何设置cPanel主机管理系统
```
    1.找到webhosting,点击setuping,填入购买的域名，
    2.选择ssl证书，
    3.选择data center（数据存储位置）,
    4.选项create wordpress,选择no thanks
    5.等待系统设置cPanel,完成后自动跳转页面，（cPanel Admin）
    6.
```
3. 如何安装wordpress
```
    1.点击cPanel Admin,进入页面，点击安装wordpress
    2.系统提醒更改设置，保持大部分设置，填写管理员账号 密码 email,website title,website Tagline,
    3.abc.com/wp-admin,登录后台，管理网站

```
4. 如何设置SSL加密
```
    1.查看webhosting添加过的证书，找到ssl certificates,点击manage
    2.页面跳转后,将语言改为简体中文，点击activate,复制code
    3.回答wordpress仪表盘，点击settings,修改wordpress地址、站点地址，从http > https，保存更改
    4.系统logout之后，重新登录后台管理系统
    5.查看网站前端，发现域名为https,点击锁子，可以看到ssl加密信息，说明网站已经被加密了
    6.添加插件，搜索 wp force ssl,功能是：强调所有登录的用户都去到有ssl加密的网站
    7.复制ssl code，回到wordpress后台，点击外观，选择小工具，点击页脚1，设置ssl加密认证，拖动左边文本到该选项，粘贴已复制的code
```
5. 如何制作网站
- 如何添加主题和更改设置
```
    - 、 
    参考网站：kejicollege.com
    genesis.zip主题 - 为父主题，outreach-pro - 为子主题,安装父主题或者父主题+子主题，（单独子主题不可用）
    此处安装genesis和子主题才可用
    二 、
    1.更改网站链接，settings中，更改网站的固定链接，在文章名处，更改为sample-post
    2.删除自动生成的文章，移动至回收站，清空回收站
    3.点击页面，选择所有页面，将不需要的页面移至回收站，
```
- 如何添加插件
```
    1.将genesis主题通过安装插件翻译为中文，搜索genesis translate
    2. 添加表格插件 contact form 7, 安装-启用
```
- 如何添加文章和页面
```
    点击文章，写文章
    1.标题 内容 分类 链接 特色图片
    2.发布，设置固定链接
    3.添加幻灯片插件，搜索genesis responsive slide
    添加页面
    添加菜单
```
- 其他
``` 
    1.如何添加sub footer
    2. 如何添加侧边栏
    3. 如何添加页脚
    4. 如何改变脚注
    
```
- 如何添加菜单 


3. 如何安装wordpress和设置主题
4. 如何改变脚注
- 安装cpanel,安装wordpress,主机ssl,ssl认证，更改网站两个网址为https,https，然后setting设置添加文本，添加ssl的code
- 如何安装wordpress
- 安装插件
- 查看博客前端页脚是否有ssl认证
- 设置wordpress网站
