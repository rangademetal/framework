import sys
sys.path.insert(0, 'F:\PichuDB\Database')

from attribution import Attribution
from schema import Schema


if __name__ == '__main__':
    database = "ID PRIMARY KEY,last_name STR(30)"
    Attribution(database, Schema('test').create_schema()).get_attribution()
