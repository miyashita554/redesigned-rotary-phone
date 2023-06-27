# 比較演算子
# 「==」は「左辺と右辺が等しい」を意味する

# 「!」は「等しくない」を意味する

#  「<(小なり)」は「より小さい」を意味する

# 「<=」は「以下」を意味する

# 「>(大なり)」は「より大きい」を意味する

# 「>=」は「以上」を意味する

# numはnumber(数値)
num = 5
if num == 3 :
    print("numは3です")
if num >= 4 :
    print("numは4以上です")
if num > 2 :
    print("numは2より大きいです")
    
num = 2
if num == 1 :
    print("numは1です。")
print("おわり") 
# この行は常に実行される  
   
# 条件に対して偽の時にだけ実行
num == 2
if num == 1 :
    print("numは1です")
else :
    print("numは1ではありません")
print("おわり")

num = 2
if num == 1 :
    print("ifのブロックに入りました")
    print("numは1です")
else :
    print("elseのブロックに入りました")
    print("numは1です")
print("おわり")
        
    
    