phone_list={"manal":"777777777",
            "manar":"777777111",
            "rahma":"777777222",
            "hala":"777777333",}

print(" 1-View numbers\n 2-Add a number\n 3-Update a number\n 4-Delete a number\n")

allitems=phone_list.items()
def View_numbers():
    for phone_key, phone_value in phone_list.items():
        print(f"{phone_key} => {phone_value}")
def Add_number():
    name=input("Enter the name")
    if name not in phone_list:
      num=input("Enter the number")
      phone_list.update({name:num})
      print("The number is added")
      View_numbers()
    else:
        print("this name is exist")
def Update_numbers():
    name=input("Enter the name you want to update")
    if name in phone_list:
       new_num=input(f"Enter the new number for{name}")
       phone_list[name]=new_num
       View_numbers()
    else:
        print("not found!")
def Delete_number():
    name=input("Enter the name you want to delete")
    if name in phone_list:
      print(phone_list.pop(name))
      print(f"{name} was deleted")
      View_numbers()
    else:
      print("is not found")
     
user_choice=input("Chose a number:")

if user_choice =="1":
    View_numbers()
elif user_choice =="2":
    Add_number()
elif user_choice =="3":
    Update_numbers()
elif user_choice =="4":
    Delete_number()
else:
    print("wrong choice!")
    
    


    




