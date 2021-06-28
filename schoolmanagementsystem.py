import csv

def write_into_csv(info_list):
    with open('student_info.csv','a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", " Contact Number", "E-Mail ID"])

        writer.writerow(info_list)

if __name__  == '__main__':
    condtion = True

    student_num = 1

    while(condtion):
        student_info =input("Enter the Student #{} Infromation as ['Name Age Contact_Number Email_ID'] : ".format(student_num))

        print(student_info)
        student_info_list = student_info.split(' ')
        print("\nThe entered information is -\nName: {}\nAge: {}\nContact_Number: {}\nE-Mail ID: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        choice_check = input("Is the entered information correct? (yes/no): ")
        if choice_check == 'yes':
            write_into_csv(student_info_list)

            condtion_check = input("Enter (yes/no) if you want to enter informtion for another students: ")
            if condtion_check == "yes":
                condtion = True
                student_num = student_num + 1
            elif condtion_check == "no":
                condtion = False

        elif choice_check == 'no':
            print("\nPlease re-enter the values!")
