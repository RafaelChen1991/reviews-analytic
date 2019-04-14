data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		#if count % 100000 == 0:
			#print(len(data))

c = 0

for datalen in data:
	c += len(datalen)

#print('留言的平均長度為',c/len(data))

wc = {} # word_count

for d in data:
	words = d.split() #預設值就為空白鍵，且遇到連續空白也可切，而不會變成控制串''
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key 進字典


for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請問你想查什麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為:', wc[word])
	else:
		print('這個字沒有出現過喔!')

print('感謝使用查詢功能')

	