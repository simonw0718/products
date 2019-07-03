import os #作業系統 operation system,可以和電腦溝通

products = [] #放在最外面，如果else fail還是可以用
if os.path.isfile('products.csv'):
    print('yeah')
# 如果不在同一資料夾就需要完整路徑,同資料夾就可以相對路徑
# os模組 的path 模組 的 isfile 功能

#讀取檔案
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue #繼續,跳到下一回,並沒有跳出迴圈
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)

else:
	print('找不到檔案...開始新帳本')


#讓使用者輸入

while True:
    name = input('請輸入商品名稱')
    if name == 'q': #quit
        break
    price = input('請輸入價格')
    products.append([name, price])
print(products)
print(products[0][0])

#印出所有購買紀錄

for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')


