print("Generation Generator")
year_born = int(input("In what year were you born? "))

if year_born >= 1925 and year_born <= 1946:
  print(f"As someone who was born in {year_born}, you are considered part of the traditionalist generation.")
elif year_born >= 1947 and year_born <= 1964:
  print(f"As someone who was born in {year_born}, you are considered part of the Baby Boomer generation.")
elif year_born >= 1965 and year_born <= 1981:
  print(f"As someone who was born in {year_born}, you are considered part of the Generation X generation.")
elif year_born >= 1982 and year_born <= 1995:
  print(f"As someone who was born in {year_born}, you are considered part of the Millenial generation.")
elif year_born >= 1996 and year_born <= 2015:
  print(f"As someone who was born in {year_born}, you are considered part of the Generation Z generation.")
else:
  print(f"As someone born in {year_born}, you don't live in a generation with a name.")