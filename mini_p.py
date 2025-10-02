


manu={
    'coffee':80,
    'pasta':50,
    'Burger':100,
    'salad':30,
    'chips':60,
    'cake':250,
    'Round mils':300,
    'Butterchicken':650,
    'palak paneer':120,
    'oranege-juice':200
}
print("...WEL_COME TO THE Resturant-MANAGEMENT SYSTEM...")

print("coffee:Rs80\npasta:Rs50\nBurger:Rs100\nsalad:Rs30\nchips:Rs60\ncake:250")

total_order=0

iteam_1=input("Order in iteam in one-iteam: ")
if iteam_1 in manu:
   
    total_order+=manu[iteam_1]
    
    print("Your iteam is successfully order..!😋")
else:
    print(f"Soory..! {iteam_1} is not available in this time 😒..try another iteam.")
while True:
    another_iteam=input("Do you want to aniother iteam(yes/no): ")
    if (another_iteam=="yes"):
        print("Order your another iteam: ")
        iteam_2=input("Enter the second iteams: ")
        if iteam_2 in manu:
            print("Your iteams is successfully ordered..!😋")
            total_order+=manu[iteam_2]
        else:
            print("plz..! Try to another iteams..")
           
    elif(another_iteam=="no"):
        print("Thanks ..! your conformation..❤️")
    print(f"your total bill is {total_order}")
    # break



