n = int(input())
word = input()
big_A = ord("А")
big_Ya = ord("Я")
smal_a = ord("а")
smal_ya = ord("я")
shifr = ""
for b in word:
    code_b = ord(b)
    if  code_b >= big_A and code_b <= big_Ya :
        code_b = (code_b - big_A + n) % 32 + big_A
    elif code_b >= smal_a and code_b <= smal_ya:
        code_b = (code_b - smal_a + n) % 32 + smal_a
    shifr += chr(code_b)
print(shifr)