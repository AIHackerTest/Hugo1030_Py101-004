#-*-coding:utf-8 -*-

# 初始化，创建文件对象和字典类型
weather_dic = {}
history_dic = {}

# 读取文件，将内容存入字典
with open('weather_info.txt') as file:
    for info in file.readlines():
        city, weather = info.split(',')
        weather_dic[city] = weather
# 按行读入，查询判断。
while True:
    order = input('请输入指令或您要查询的城市名：')
    # 查询城市天气，并将查询结果存入字典
    if order in weather_dic.keys():
        weather = weather_dic[order]
        history_dic[order] = weather #保存查询结果
        print('{}的天气状况为：{}'.format(order, weather))

    # 查询帮助信息
    elif order in ['h', 'help']:
        print(
        '''
            输入城市名，查询该城市的天气；
            输入 help, 获取帮助文档；
            输入 history, 获取查询历史；
            输入 quit, 退出天气查询系统。
        '''
        )

    # 查询历史记录
    elif order in ['history']:
        for order in history_dic:
            print(order, history_dic[order])

    # 返回历史记录，退出程序
    elif order in ['quit', 'q']:
        print("显示查询结果，退出程序！")
        for order in history_dic:
            print(order, history_dic[order])
        break

    else:
        print('没有该城市信息!请输入help查看帮助文档。')
