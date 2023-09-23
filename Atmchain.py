
# Цепочка обязанностей (Chain of Responsibility): передает запрос по цепочке потенциальных обработчиков,
# пока он не будет обработан или цепочка не закончится.
# Пример с подбором номинала при выдаче запрошенной суммы из банкомата

class DispenseChain:
    def set_next_chain(self, next_chain):
        pass

    def dispense(self, cur):
        pass

class Dollar100Dispenser(DispenseChain):
    def __init__(self):
        self.chain = None

    def set_next_chain(self, next_chain):
        self.chain = next_chain

    def dispense(self, cur):
        if cur.amount >= 100:
            num = cur.amount // 100
            remainder = cur.amount % 100
            print("Выдается(ются) {}  банкнот(а) номиналом 100$".format(num))
            if remainder != 0:
                self.chain.dispense(Currency(remainder))
        elif self.chain:
            self.chain.dispense(cur)

class Dollar50Dispenser(DispenseChain):
    def __init__(self):
        self.chain = None

    def set_next_chain(self, next_chain):
        self.chain = next_chain

    def dispense(self, cur):
        if cur.amount >= 50:
            num = cur.amount // 50
            remainder = cur.amount % 50
            print("Выдается(ются) {}  банкнот(а) номиналом 50$".format(num))
            if remainder != 0:
                self.chain.dispense(Currency(remainder))
        elif self.chain:
            self.chain.dispense(cur)

class Dollar20Dispenser(DispenseChain):
    def __init__(self):
        self.chain = None

    def set_next_chain(self, next_chain):
        self.chain = next_chain

    def dispense(self, cur):
        if cur.amount >= 20:
            num = cur.amount // 20
            remainder = cur.amount % 20
            print("Выдается(ются) {}  банкнот(а) номиналом 20$".format(num))
            if remainder != 0:
                self.chain.dispense(Currency(remainder))
        elif self.chain:
            self.chain.dispense(cur)

class Dollar10Dispenser(DispenseChain):
    def __init__(self):
        self.chain = None

    def set_next_chain(self, next_chain):
        self.chain = next_chain

    def dispense(self, cur):
        if cur.amount >= 10:
            num = cur.amount // 10
            remainder = cur.amount % 10
            print("Выдается(ются) {}  банкнот(а) номиналом 10$".format(num))
            if remainder != 0:
                self.chain.dispense(Currency(remainder))
        elif self.chain:
            self.chain.dispense(cur)

class Dollar5Dispenser(DispenseChain):
    def __init__(self):
        self.chain = None

    def set_next_chain(self, next_chain):
        self.chain = next_chain

    def dispense(self, cur):
        if cur.amount >= 5:
            num = cur.amount // 5
            remainder = cur.amount % 5
            print("Выдается(ются) {}  банкнот(а) номиналом 5$".format(num))
            if remainder != 0:
                self.chain.dispense(Currency(remainder))
        elif self.chain:
            self.chain.dispense(cur)

class Dollar1Dispenser(DispenseChain):
    def __init__(self):
        self.chain = None

    def set_next_chain(self, next_chain):
        self.chain = next_chain

    def dispense(self, cur):
        if cur.amount >= 1:
            num = cur.amount // 1
            remainder = cur.amount % 1
            print("Выдается(ются) {}  банкнот(а) номиналом 1$".format(num))
            if remainder != 0:
                self.chain.dispense(Currency(remainder))
        elif self.chain:
            self.chain.dispense(cur)

class Currency:
    def __init__(self, amount):
        self.amount = amount

class ATMDispenser:
    def __init__(self):
        self.chain1 = Dollar100Dispenser()
        self.chain2 = Dollar50Dispenser()
        self.chain3 = Dollar20Dispenser()
        self.chain4 = Dollar10Dispenser()
        self.chain5 = Dollar5Dispenser()
        self.chain6 = Dollar1Dispenser()

        self.chain1.set_next_chain(self.chain2)
        self.chain2.set_next_chain(self.chain3)
        self.chain3.set_next_chain(self.chain4)
        self.chain4.set_next_chain(self.chain5)
        self.chain5.set_next_chain(self.chain6)

    def dispense(self, cur):
        self.chain1.dispense(cur)

atm = ATMDispenser()
print("Введите требуемую сумму: ")
ammount = int(input())
atm.dispense(Currency(ammount))
