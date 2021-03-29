#輸入密碼 並擁有3次驗證機會

password = 'a123456'
i = 3 # 剩下機會
#while True: # 高階 i>0
while i > 0:
	pwd = input('PWD = ? ')
	if pwd == password:
		print('OK!')
		break
	else:
		i = i-1
		print('Wrong, U have only' , i, 'chance')
		#if i == 0: # 高階 不用寫
		#	break # 高階 不用寫