value = input("身長をcmで入力してください：")
tall = float(value)
print("身長：",tall,"cm")
value = input("体重をkgで入力してください：")
weight = float(value)
print("体重",weight,"kg")
bmi =  round(weight / ((tall / 100) * (tall / 100)),2)
print("BMIは",bmi,"で")
if bmi > 25:
    hantei = '肥満'
elif bmi >= 18.5:
    hantei = '標準'
else:
    hantei = '痩せ'
print("判定は",hantei)
print("適正体重は",round(((tall / 100) * (tall / 100) * 22),2),"kgです")