text = "X-DSPAM-Confidence:    0.8475"
pos  = text.find('0')
ans = text[pos:]
num = float(ans)
print(num)