a = input("a = ").split()
b = input("b = ").split()
print("#" * 20)
A = set(a)
B = set(b)
print(f'a = {A}')
print(f'b = {B}')
print(f'합집합: {A | B}')
print(f'교집합: {A & B}')
print(f'차집합: {A - B}')