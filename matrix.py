import sys

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to Hide a Treasure App!! ")
print("\t\t\t\t\t\t\t\t\t\tWe are trust worthy, you just have to enter 2 digit number in the matrix below:\n")

rembo1 = ['❌','❌','❌']
rembo2 = ['❌','❌','❌']
rembo3 = ['❌','❌','❌']

combi = [rembo1,rembo2,rembo1]
print(f"{rembo1}\n{rembo2}\n{rembo3}")

markX = input("Enter the row & column(No comma) of your choice within the matrix: ")#string
#convert to int
row = int(markX[0])#accessing the first digit using the indexing method
col = int(markX[1])#accessing the second digit using the indexing method
#
selectedRow = combi[row-1]
selectedRow[col-1] = '✔️'
print(f"{rembo1}\n{rembo2}\n{rembo3}")
print("Yohhhh well done champ you did it!!")
print("Your treasure is safe with us...")

print(f"Kindly rate us: \n"
      f"1. ⭐️⭐️⭐️⭐️⭐️\n"
      f"2. ⭐️⭐️⭐️⭐️\n"
      f"3. ⭐️⭐️⭐️\n"
      f"4. ⭐️⭐️\n"
      f"5. ⭐️")

ratings = int(input("Enter your ratings:  "))
if ratings == 1:
    print("😘👍💯☺️ Highly Appreciated.")
elif ratings == 2:
    print("😇 Great.")
elif ratings == 3:
    print("🙂 Good.")
elif ratings == 4:
    print("😐 Alright.")
else:
    print("😥 Okay.")

sys.exit()
