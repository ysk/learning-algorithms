# coding: utf-8

print("「A」のUnicode：", ord('A'))
print("「あ」のUnicode：", ord('あ'))
print("「33」のUnicode：", chr(33))
print("「12356」のUnicode：", chr(12356))
print("----------------------")

while True:
    s = input("1文字入力してください")
    if len(s) != 1:
        break
    print(s+"のUnicode：", ord(s))
