from datetime import datetime
from application.salary import print_salary
from application.db.people import print_people
import spotify

if __name__ == '__main__':
    print_salary('main_salary')
    print_people('main_people')
    print(datetime.now())
    print(datetime.today())