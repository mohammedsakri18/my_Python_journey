amount = int(input("Enter amount: "))

note_500 = amount // 500
remaining_amount = amount % 500

note_200 = remaining_amount // 200
remaining_amount = remaining_amount % 200

note_100 = remaining_amount // 100
remaining_amount = remaining_amount % 100

print(f"500 Notes: {note_500}")
print(f"200 Notes: {note_200}")
print(f"100 Notes: {note_100}")
print(f"Remaining Amount: {remaining_amount}")