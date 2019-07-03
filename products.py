import os #開啟os可以跟電腦溝通
#讀取檔案
def read_file(filename):
    products = [] #放在最外面，如果else fail還是可以用
    with open(filename, 'r', encoding = 'utf-8') as f:
            for line in f:
                if '商品,價格' in line:
                    continue #繼續,跳到下一回,並沒有跳出迴圈
                name, price = line.strip().split(',')
                products.append([name, price])
    return products

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱')
        if name == 'q': #quit
            break
        price = input('請輸入價格')
        products.append([name, price])
    print(products)
    print(products[0][0])
    return products
#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

#function中心思想:只做一件事情

def main(filename):
    if os.path.isfile(filename): #檢查檔案在不
        print('yeah')
    # 如果不在同一資料夾就需要完整路徑,同資料夾就可以相對路徑
    # os模組 的path 模組 的 isfile 功能
        products = read_file(filename)
    else:
        print('找不到檔案...開始新帳本')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main('products.csv')

# 整個改寫成function的過程稱為refactor 重構