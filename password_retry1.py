password = 'a123456'
c = 3
while c > 0:
	c -= 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登錄成功')
		break
	else:
		if c > 0:
			print('輸入錯誤!還剩',c,'次機會')
		else:
			print('密碼錯誤! 不能再試了!')

