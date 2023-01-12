import sqlalchemy
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Date, CHAR
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

hostname = 'localhost'
database = 'lab1'
username = 'postgres'
pwd = 'password'
port_id = 5432

Base = declarative_base()

def get_engine():
    return create_engine(url = f"postgresql://{username}:{pwd}@{hostname}:{port_id}/{database}")


class company(Base):
    __tablename__ = "company"
    cid = Column(Integer, primary_key = True)
    name = Column(String)
    foundation_date = Column(Date)



class office(Base):
    __tablename__ = "office"
    oid = Column(Integer, primary_key = True)
    company_id = Column(Integer, ForeignKey("company.cid"))
    placement = Column(String)
    purpose = Column(String)



class employer(Base):
    __tablename__ = "employer"
    eid = Column(Integer, primary_key = True)
    office_id = Column(Integer, ForeignKey("office.oid"))
    name = Column(String)
    gender = Column(CHAR)
    date_of_birth = Column(Date)



class project(Base):
    __tablename__ = "project"
    pid = Column(Integer, primary_key = True)
    name = Column(String)
    creation_date = Column(Date)



class project_worker(Base):
    __tablename__ = "project_worker"
    project_id = Column(Integer, ForeignKey("project.pid"), primary_key = True)
    employer_id = Column(Integer, ForeignKey("employer.eid"), primary_key = True)



engine = get_engine()

Session = sessionmaker(bind=engine)
s = Session()

def refreh():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def insert_company(cidd, namee, foundation_datee):
    compan = company(
    cid = cidd,
    name = namee,
    foundation_date = foundation_datee
    )
    s.add(compan)
    s.commit()

def insert_office(oidd, company_idd, placementt, purposee):
    offic = office(
        oid = oidd,
        company_id = company_idd,
        placement = placementt,
        purpose = purposee
    )
    s.add(offic)
    s.commit()

def insert_employer(eidd, office_idd, namee, genderr, date_of_birthh):
    employe = employer(
        eid = eidd,
        office_id = office_idd,
        name = namee,
        gender = genderr,
        date_of_birth = date_of_birthh
    )
    s.add(employe)
    s.commit()

def insert_project(pidd, namee, creation_datee):
    projec = project(
        pid = pidd,
        name = namee,
        creation_date = creation_datee
    )
    s.add(projec)
    s.commit()

def insert_project_worker(project_idd, employer_idd):
    project_worke = project_worker(
        project_id = project_idd,
        employer_id = employer_idd
        
    )
    s.add(project_worke)
    s.commit()

def delete_employer_name(namee):
    employes = s.query(employer).filter(employer.name == namee).first()
    s.query(project_worker).filter(project_worker.employer_id == employes.eid).delete()
    s.delete(employes)
    s.commit()

def delete_employer_id(eidd):
    employes = s.query(employer).filter(employer.eid == eidd).first()
    s.query(project_worker).filter(project_worker.employer_id == employes.eid).delete()
    s.delete(employes)
    s.commit()

def delete_employer_office_id(off_id):
    employes = s.query(employer).filter(employer.office_id == off_id).first()
    s.query(project_worker).filter(project_worker.employer_id == employes.eid).delete()
    s.query(project_worker).filter(project_worker.employer_id == employes.eid).delete()
    s.delete(employes)
    s.commit()

def delete_employer_all(namee):
    while 1:
        try:
            emp = s.query(employer).filter(employer.name == namee).first()
            s.query(project_worker).filter(project_worker.employer_id == emp.eid).delete()
            s.delete(emp)
            s.commit()
        except:
            break

def delete_office(oidd):
    while 1:
        try:
            delete_employer_office_id(oidd)
        except:
            break
    offic = s.query(office).filter(office.oid == oidd).first()
    s.delete(offic)
    s.commit()

def delete_project_worker(prj_id, emp_id):
    s.query(project_worker).filter(project_worker.employer_id == emp_id, project_worker.project_id == prj_id).delete()
    s.commit()

def delete_project(prj_id):
    prj = s.query(project).filter(project.pid == prj_id).first()
    s.query(project_worker).filter(project_worker.project_id == prj.pid).delete()
    s.delete(prj)
    s.commit()


def update_office_placement(o_id, new_placement):
    off = s.query(office).filter(office.oid == o_id).first()
    off.placement = new_placement
    s.commit()

def update_office_purpose(o_id, new_purpose):
    off = s.query(office).filter(office.oid == o_id).first()
    off.purpose = new_purpose
    s.commit()

def update_employer_name(emp_id, new_name):
    emp = s.query(employer).filter(employer.eid == emp_id).first()
    emp.name = new_name
    s.commit()

def update_employer_gender(emp_id, new_gender):
    emp = s.query(employer).filter(employer.eid == emp_id).first()
    emp.gender = new_gender
    s.commit()

def update_employer_date_of_birth(emp_id, new_date):
    emp = s.query(employer).filter(employer.eid == emp_id).first()
    emp.date_of_birth = new_date
    s.commit()

def update_employer_office_id(emp_id, new_oid):
    emp = s.query(employer).filter(employer.eid == emp_id).first()
    emp.office_id = new_oid
    s.commit()

def update_project_name(prj_id, new_name):
    prj = s.query(project).filter(project.pid == prj_id).first()
    prj.name = new_name
    s.commit()

def update_project_creation_date(prj_id, new_date):
    prj = s.query(project).filter(project.pid == prj_id).first()
    prj.creation_date = new_date
    s.commit()



def insert_in_office():
    off_id = int(input('enter office_id: '))
    com_id = int(input('enter company_id: '))
    placement = input('enter placement: ')
    purpose = input('enter purpose: ')
    insert_office(off_id, com_id, placement, purpose)

def delete_from_office():
    off_id = int(input('enter office_id: '))
    delete_office(off_id)

def update_office_data():
    print("update: 1 - placement, 2 - purpose")
    choice = int(input('enter choice: '))
    if choice == 1:
        off_id = int(input('enter office_id: '))
        new_placement = input('enter new_placement: ')
        update_office_placement(off_id, new_placement)
    if choice == 2:
        off_id = int(input('enter office_id: '))
        new_purpose = input('enter new_purpose: ')
        update_office_placement(off_id, new_purpose)


def insert_in_employer():
    emp_id = int(input('enter employer_id: '))
    off_id = int(input('enter office_id: '))
    name = input('enter name: ')
    gender = input('enter gender: ')
    dob = input('enter date_of_birth:' )
    insert_employer(emp_id, off_id, name, gender, dob)

def delete_from_employer():
    print("delete BY: 1 - name(delete first), 2 - name(delete all), 3 - employer_id")
    choice = int(input('enter choice: '))
    if choice == 1:
        name = input('enter name: ')
        delete_employer_name(name)
    if choice == 2:
        name = input('enter name: ')
        delete_employer_all(name)
    if choice == 3:
        emp_id = input('enter employer_id: ')
        delete_employer_id(emp_id)

def update_employer_data():
    print("update: 1 - office_id, 2 - name, 3 - gender, 4 - date_of_birth")
    choice = int(input('enter choice: '))
    if choice == 1:
        emp_id = int(input('enter employer_id: '))
        off_id = int(input('enter new office_id: '))
        update_employer_office_id(emp_id, off_id)
    if choice == 2:
        emp_id = int(input('enter employer_id: '))
        name = input('enter new name: ')
        update_employer_name(emp_id, name)
    if choice == 3:
        emp_id = int(input('enter employer_id: '))
        gender = input('enter new gender: ')
        update_employer_gender(emp_id, gender)
    if choice == 4:
        emp_id = int(input('enter employer_id: '))
        dob = input('enter new date_of_birth: ')
        update_employer_date_of_birth(emp_id, dob)


def insert_in_projcet_worker():
    prj_id = int(input('enter project id: '))
    emp_id = int(input('enter employer_id: '))
    insert_project_worker(prj_id, emp_id)

def delete_from_project_worker():
    prj_id = int(input('enter project id: '))
    emp_id = int(input('enter employer_id: '))
    delete_project_worker(prj_id, emp_id)


def insert_in_project():
    prj_id = int(input('enter project id: '))
    name = input('enter name: ')
    creation_date = input('enter creation_date: ')
    insert_project(prj_id, name, creation_date)

def delete_from_project():
    prj_id = int(input('enter project id: '))
    delete_project(prj_id)

def update_project_data():
    print("update: 1 - name, 2 - creation_date")
    choice = int(input('enter choice: '))
    if choice == 1:
        prj_id = int(input('enter project id: '))
        name = input('enter new name: ')
        update_project_name(prj_id, name)
    if choice == 2:
        prj_id = int(input('enter project id: '))
        creation_date = input('enter new creation_date: ')
        update_project_creation_date(prj_id, creation_date)



def initial_data():
    insert_company(1, 'Sus', '2003-02-01')

    insert_office(1, 1, "somewhere", "training")
    insert_office(2, 1, "second", "second")
    insert_office(3, 1, "third", "third")

    insert_employer(1, 1, "Sasha", 'M', '2000-12-01')
    insert_employer(2, 1, "Masha", 'F', '2000-12-01')
    insert_employer(3, 2, "Masha", 'F', '2003-12-01')

    insert_project(1, "project1", '2001-01-01')
    insert_project(2, "project2", '2002-01-01')

    insert_project_worker(1, 2)
    insert_project_worker(1, 1)
    insert_project_worker(1, 3)
    insert_project_worker(2, 3)


def close_session():
    s.close()




#def __repr__(self):
#    return "<company(cid = '{}', name = '{}', foundation_date = '{}')>"\
#            .format(self.cid, self.name, self.foundation)



