# 以下是类模型定义部分


# 购物车模型
class ChartList:
    def __init__(self, id, name, price, count):
        self.id = id
        self.name = name
        self.price = price
        self.count = count


# 订单模型
class OrderList:
    def __init__(self, id, good_id, name, price, count):
        self.id = id
        self.good_id = good_id
        self.name = name
        self.price = price
        self.count = count


# 总订单模型
class OrdersList:
    def __init__(self, id, create_time):
        self.id = id
        self.create_time = create_time

    def set_prices(self, prices):
        self.prices = prices
