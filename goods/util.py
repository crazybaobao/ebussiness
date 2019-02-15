from django.shortcuts import get_object_or_404
from goods.models import Goods, Order, Orders, User
from goods.object import ChartList, OrderList, OrdersList
import hashlib


class Util:
    # 检查用户是否登录
    @staticmethod
    def check_user(request):
        # 从cookies中取出username，不存在则返回空字符
        username = str(request.session.get('username', ''))
        # 判断在user表中是否存在
        user = User.objects.filter(username=username)
        # 如果不存在，返回空串
        if user is None:
            return ""
        # 否则返回username
        else:
            return username

    # MD5加密
    @staticmethod
    def md5(my_str):
        # 判断是否是字符串
        if isinstance(my_str, str):
            m = hashlib.md5()
            m.update(my_str.encode('utf8'))
            return m.hexdigest()
        else:
            return ""

    # 通过order_id判断这个订单是否属于当前登录用户
    @staticmethod
    def check_user_by_order(username, order_id):
        # 获取order_id对应的order信息
        order = get_object_or_404(Order, id=order_id)
        # 通过username获取对应的user信息
        user = get_object_or_404(User, username=username)
        if order.user_id == user.id:
            return 1
        else:
            return 0

    # 返回购物车内商品的个数
    @staticmethod
    def cookies_count(request):
        # 返回本地所有的cookie
        cookie_list = request.COOKIES
        # 只要进入网站，系统中就会产生一个名为sessionid的cookie
        # 如果后台同时在运行，会产生一个名为csrftoken的cookie
        length = len(request.COOKIES)
        for i in cookie_list:
            if (i == "csrftoken") or (i == "sessionid") or (i.startswith("Hm_lvt_")) or (i.startswith("Hm_lpvt_")):
                length = length - 1
        return length

    # 获取购物车内的所有内容
    @staticmethod
    def deal_cookies(request):
        # 获取本地所有内COOKIES
        cookie_list = request.COOKIES
        # 去除COOKIES内的sessionid
        cookie_list.pop("sessionid")
        # 如果COOKIES内含有csrftoken，去除COOKIES内的csrftoken
        for key in list(cookie_list.keys()):
            if (key == "csrftoken") or (key == "sessionid") or (key.startswith("Hm_lvt_")) or (
                    key.startswith("Hm_lpvt_")):
                del cookie_list[key]
        # 返回处理好的购物车内的所有内容
        return cookie_list

    # 加入购物车
    def add_chart(self, request):
        # 获取购物车内的所有内容
        cookie_list = self.deal_cookies(request)
        # 定义my_chart_list列表
        my_chart_list = []
        # 遍历cookie_list，把里面的内容加入类Chart_list列my_chart_list中
        for key in cookie_list:
            chart_object = ChartList
            chart_object = self.set_chart_list(key, cookie_list)
            my_chart_list.append(chart_object)
        # 返回 my_chart_list
        return my_chart_list

    # 定义单个订单变量
    @staticmethod
    def set_order_list(key):
        good_list = get_object_or_404(Goods, id=key.goods_id)
        order_list = OrderList(key.id, good_list.id, good_list.name, good_list.price, key.count)
        return order_list

    @staticmethod
    def set_orders_list(key):
        order_list = OrdersList(key.id, key.create_time)
        return order_list

    # 把获取的购物车中的商品放在一个名为Chart_list()的类中，返回给模板
    @staticmethod
    def set_chart_list(key, cookie_list):
        good_list = get_object_or_404(Goods, id=key)
        chart_list = ChartList(key, good_list.name, good_list.price, cookie_list[key])
        return chart_list
