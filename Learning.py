def disease():
    dis = input("Enter medical issues: ")
    if dis.lower() in dis_list1:
        if dis.lower() == dis_list1[0]:
            print("Take this <prescription>")
        elif dis.lower() == dis_list1[1]:
            print("Take this <prescription>")
        elif dis.lower() == dis_list1[2]:
            print("Take this <prescription>")
        elif dis.lower() == dis_list1[3]:
            print("Take this <prescription>")
    elif dis.lower() in dis_list2:
        if dis.lower() == dis_list2[0]:
            print("Please consult this <Doctor's name>")
        elif dis.lower() == dis_list2[1]:
            print("Please consult this <Doctor's name>")
        elif dis.lower() == dis_list2[2]:
            print("Please consult this <Doctor's name>")
        elif dis.lower() == dis_list2[3]:
            print("Please consult this <Doctor's name>")
    elif dis.lower() not in dis_list1 and dis.lower() not in dis_list2:
        print("The entered medical issue is currently not available.")
        print("Sorry for the inconvenience caused")
    print("\nThank you for using our service.")


a = 1
while a == 1:
    dis_list1 = ['cold', 'fever', 'cough', 'headaches']
    dis_list2 = ['cancer', 'pneumonia', 'stroke', 'chicken pox']
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age < 20:
        user_inp_1 = int(input("\nChild or Teen (1/2): "))
        if user_inp_1 == 1:
            disease()
        elif user_inp_1 == 2:
            disease()
    if age > 20:
        disease()
    a = int(input("Continue or not? (1/2): "))
    print()
