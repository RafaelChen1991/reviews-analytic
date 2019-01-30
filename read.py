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


print(c/len(data))
	


##print很耗時