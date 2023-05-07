import sys
sys.path.insert(0, 'F:\PichuDB\Database')

from attribution import Attribution
from schema import Schema


if __name__ == '__main__':
    database = "ID_test PRIMARY KEY AUTO INCREMENT, last_name STR(30)"
    print(database)
    Attribution(
        database,
        Schema('test').create_schema(),
        Schema('test').create_table('Student')
    ).get_attribution()
    print()
