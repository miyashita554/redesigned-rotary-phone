# クラスの定義
class CharaTest:
    def __init__(self, name):
        self.name = "name"
    def fight(self):
        print(self.name + "戦うぞ!")
        
# クラスの使用
chara1 = CharaTest("戦士")
print(chara1.name)
chara1.fight()