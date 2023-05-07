import sys
sys.path.insert(0, 'F:\PichuDB\Database')

from attribution import Attribution
from schema import Schema


if __name__ == '__main__':
    database = "ID_test PRIMARY KEY AUTO INCREMENT, last_name STR(30), firstname STR(40)"
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
