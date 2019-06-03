# my_flask

项目依赖环境：

MySQL 5.6

python 3.7

搭建过程：

1. 拉取代码
2. virtualenv venv
3. . venv/bin/activate
4. pip install -r requements.txt
5. cp .env. example .env
6. vim .env 修改环境变量：注意修改DEBUG相关的环境变量和项目依赖的第三方地址
7. make init  初始化migration
8. make migrate
9. make upgrade
10. 项目启动honcho start
11. 项目调试 hocho run ipython
12. 运行脚本 honcho run ipython -m tools.test.py, 也可以在 honcho run ipython 之后调用方法
