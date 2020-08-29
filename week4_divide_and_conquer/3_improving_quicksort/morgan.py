text = "hello world"
ans = ""
for i in range(len(text)):
    if text[i-1] == " " and i!= len(text)-1:
        ans += text[i].capitalize()
    else:
        ans += text[i]

print(ans)
