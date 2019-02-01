data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))

c = 0

for datalen in data:
	c += len(datalen)


print('留言的平均長度為',c/len(data))
##print很耗時

new = []
for datanew in data:
	if len(datanew) < 100:
		new.append(datanew)

print('一共有',len(new),'筆資料，留言長度小於100')

print(new[0])
