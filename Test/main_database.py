import sys

sys.path.insert(0, 'F:\PichuDB\Database')

from attribution import Attribution
from schema import Schema

if __name__ == '__main__':
    database = "ID_test PRIMARY KEY AUTO INCREMENT, " \
               "last_name STR(30) UNIQUE, " \
               "firstname STR(43) NOT NULL, " \
               "istrue BOOLEAN default=false," \
               "age INTEGER(7)," \
               "test_int INTEGER(13) NOT NULL," \
               "date_create DATE NOT NULL," \
               "datetime_create DATETIME NOT NULL," \
               "test_float FLOAT"
    print(database)
    print(Schema('test').create_schema())
    Student = Schema('test').create_table('Student')
    Professor = Schema('test').create_table('Professor')
    print(Student)
    Attribution(
        database,
        Schema('test').create_schema(),
        Student
    ).get_attribution()
    print()
