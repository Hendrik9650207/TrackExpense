import enum


# 列舉中資料的類型是用name去取用
# 列舉中資料的值則是採用value去取用
class CostType(enum.Enum):
    food = "食"
    clothing = "衣"
    housing = "住"
    transportation = "行"
    creation = "樂"

class CashFlow(enum.Enum):
    cost = "支出"
    income = "收入"
    transfer = "轉帳"


class Accounts:
    def __init__(self, mFlow: CashFlow, costType: CostType, price: int):
        self.mFlow = mFlow
        self.costType = costType
        self.price = price

    def display(self):
        print("flow:", self.mFlow.name)
        print("Type:", self.costType.name)
        print("$:", self.price)


list1 = []
list1.append(Accounts(CashFlow.cost, CostType.transportation, 1200))
list1.append(Accounts(CashFlow.cost, CostType.transportation, 500))
list1.append(Accounts(CashFlow.cost, CostType.clothing, 1700))
list1.append(Accounts(CashFlow.cost, CostType.food, 790))
list1.append(Accounts(CashFlow.cost, CostType.transportation, 1125))
list1.append(Accounts(CashFlow.cost, CostType.food, 1590))
list1.append(Accounts(CashFlow.cost, CostType.clothing, 1350))


search_Item = "衣"
search_Max = 1800
search_Min = 1200


list2 = []
for i in list1:
    # print(type(i.costType.name))
    # print(i.costType.value)

    if search_Item == i.costType.value and search_Min <= i.price <= search_Max:
        list2.append(i)
        print(i.costType.value, ":", i.price)

# print(type(search_Item))

