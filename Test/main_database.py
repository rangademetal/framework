from Database.attribution import Attribution
from Database.schema import Schema
from Settings.os_operation import OsOperation

if __name__ == '__main__':
    insert_ = "INSERT INTO Student VALUES (test)"

    database = "ID_test PRIMARY KEY AUTO INCREMENT, " \
               "last_name STR(30) UNIQUE, " \
               "firstname STR(43) NOT NULL, " \
               "istrue BOOLEAN default=false," \
               "age INTEGER(7)," \
               "test_int INTEGER(13) NOT NULL," \
               "date_create DATE NOT NULL," \
               "datetime_create DATETIME NOT NULL," \
               "test_float FLOAT"

    Student = Schema('test1').create_table('Student')

    create_database = Attribution(
        database,
        Schema('test1').create_schema(),
        Student,
        OsOperation(path=r'F:\PichuDB\Settings\Settings.json').path
    )


    create_database.get_attribution('test1')
    create_database.get_values(insert_)
