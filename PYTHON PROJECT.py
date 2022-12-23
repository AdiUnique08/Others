# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 11:11:11 2022

@author: MKS
"""

def disease():
    dis = input("\nEnter medical issues: ")
    if dis.lower() in dis_list1:
        if dis.lower() == dis_list1[0]:
            print("\nTake one tablet of Paracitamol")
        elif dis.lower() == dis_list1[1]:
            print("\nTake one tablet of Septilin ")
        elif dis.lower() == dis_list1[2]:
            print("\nTake 1 spoon of LIV52")
        elif dis.lower() == dis_list1[3]:
            print("\nApply Zandu Balm")
        elif dis.lower() == dis_list1[4]:
            print("Make use of Albuterol")
        elif dis.lower() == dis_list1[5]:
            print("Take a painkiller")
        elif dis.lower() == dis_list1[6]:
            print("Make use of eyedrops")
    elif dis.lower() in dis_list2:
        if dis.lower() == dis_list2[0]:
            print("\nPlease consult an Oncologist")
        elif dis.lower() == dis_list2[1]:
            print("\nPlease consult a Pulmonologist")
        elif dis.lower() == dis_list2[2]:
            print("\nPlease consult a Vascular Neurologist ")
        elif dis.lower() == dis_list2[3]:
            print("\nPlease consult a Rheumatologist")
        elif dis.lower() == dis_list2[4]:
            print("\nPlease consult a Endocrinologist")
        elif dis.lower() == dis_list2[5]:
            print("\nPlease consult a Pulmonologist")
    elif dis.lower() not in dis_list1 and dis.lower() not in dis_list2:
        print("\nThe entered medical issue is currently not available.")
        print("\nSorry for the inconvenience caused")
    print("\nThank you for using our service.")


a = 1
while a == 1:
    dis_list1 = ['cold', 'fever', 'cough', 'headaches','asthama',"bodypain",'conjunctivitis']
    dis_list2 = ['cancer', 'pneumonia', 'stroke', 'arthritis','Tuberculosis','Diabetes',' pulmonary disease']
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    disease()
    a = int(input("Continue or not? (1/2): "))
    print()