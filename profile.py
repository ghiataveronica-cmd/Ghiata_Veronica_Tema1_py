last_name=input("last name:")
first_name=input("first name:")
age=int(input("age:"))
city=input("city:")

name=f"{last_name} {first_name}"
length_name=len(name)
year=2026-age

print("-" * 39)
print(f"{name}, {age}")
print(f"{city}")
print(f"name length: {length_name} characteres")
print(f"born around: {year}")
print("-" * 39)



