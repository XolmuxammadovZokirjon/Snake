

yosh = int(input("Yoshingiz nechchida?"))
if yosh<= 4:
    narh = 0
elif yosh <= 12:
    narh = 5000
elif yosh <= 18:
    narh = 8000
else:
    narh = 10000
print(f"Sizga kirish {narh} so\'m")