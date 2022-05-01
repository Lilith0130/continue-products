#讀取檔案
products = []
with open('products.csv', 'r') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name,price])
print(products)		 

#讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	products.append([name, price])
print(products)	

#印出購買紀錄
for p in products:
	print(p[0],'的價格是', p[1])

#寫入檔案
with open('products.csv', 'w') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')


		