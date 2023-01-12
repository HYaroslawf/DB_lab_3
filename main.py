from config import *
from model import *






def office_():
    f = -1
    while f != 0:
        print("\nOffice table:")
        print("1 - insert\n2 - delete\n3 - update\n0 - exit")
        f = int(input('enter your choice: '))
        if f == 1:
            insert_in_office()
        if f == 2:
            delete_from_office()
        if f == 3:
            update_office_data()

def employer_():
    f = -1
    while f != 0:
        print("\nEmployer table")
        print("1 - insert\n2 - delete\n3 - update\n0 - exit")
        f = int(input('enter your choice: '))
        if f == 1:
            insert_in_employer()
        if f == 2:
            delete_from_employer()
        if f == 3:
            update_employer_data()

def project_worker_():
    
    f = -1
    while f != 0:
        print("\nproject_worker table")
        print("1 - insert\n2 - delete\n0 - exit")
        f = int(input('enter your choice: '))
        if f == 1:
            insert_in_projcet_worker()
        if f == 2:
            delete_from_project_worker()


def project_():
    f = -1
    while f != 0:
        print("\nProject table")
        print("1 - insert\n2 - delete\n3 - update\n0 - exit")
        f = int(input('enter your choice: '))
        if f == 1:
            insert_in_project()
        if f == 2:
            delete_from_project()
        if f == 3:
            update_project_data()



refreh()

initial_data()

flag = -1

while flag != 0:
    print("\nMAIN MENU\n1 - office\n2 - employer\n3 - project_worker\n4 - project\n0 - exit")
    flag = int(input('enter your choice: '))
    if flag == 1:
        office_()
    if flag == 2:
        employer_()
    if flag == 3:
        project_worker_()
    if flag == 4:
        project_()


#delete_office(3)

#delete_employer_all("Masha")
#delete_office(2)
#delete_employer_office_id(1)
#delete_office(1)
#delete_project_worker(1, 3)
#delete_project(1)

#update_office_placement(1, "here")
#update_office_purpose(2, "ordinating")

#update_employer_office_id(1, 3)

#update_project_creation_date(1, '1999-01-01')

close_session()

s.close()



print(sqlalchemy.__version__)