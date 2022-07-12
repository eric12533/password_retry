password = 'a123456'
c = 3
while c > 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登陸成功')
		break
	else:
		c -= 1
		print('輸入錯誤!還剩',c,'次機會')

