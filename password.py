inValid = True
while inValid:
  password = input("Enter your password:")
  specialCharacter = ['!','@','#','$','%','^','&','*','+','?','>']
  lower = upper = numbers = specials = 0
  length = len(password)

  if length>= 8 and length <= 16:
    for i in password:
      if i.islower():
        lower+=1
      elif i.isupper():
        upper+=1
      elif i.isdigit():
        numbers+=1
      elif i in specialCharacter:
        specials+=1

    if lower<1 or upper<1 or numbers<1 or specials<1:

      missing = []
      if lower<1:
        missing.append("Lowercase Letters,")
      if upper<1:
        missing.append("Uppercase Letters,")
      if numbers<1:
        missing.append("Numbers,")
      if specials<1:
        missing.append("Special Characters")

      print("Your password is missing:",",".join(missing))
      print("Please enter a valid password:")

    else:
      print("Your password is valid.")
      inValid = False

  else:
    print("The length of the password should be between 8 and 16. Please enter a valid password.")