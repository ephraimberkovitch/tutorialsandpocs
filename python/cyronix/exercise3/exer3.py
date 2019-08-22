import csv
import re


def normalize_number(n):

    return int(n.replace(',',''))


def get_offset_length_from_string(s):

    s = s.replace(', Priority: Normal','')
    m = re.search(r'Offset: (.+), Length: (.+)', s)
    return normalize_number(m.group(1)), normalize_number(m.group(2))


def get_all_possible_operations():
    input_file = csv.DictReader(open("/Users/ephraimberkovitch/workspace/demos/cyronix/exercise3/Logfile.CSV"))
    operations = set()
    lengths = set()
    offsets = set()
    for row in input_file:
        operations.add(row['Operation'])
        if row['Operation'] == 'ReadFile':
            offset, length = get_offset_length_from_string(row['Detail'])
            lengths.add(length)
            offsets.add(offset)
    print(operations)  # {'CloseFile', 'ReadFile', 'QueryInformationVolume', 'QueryAllInformationFile', 'CreateFile'}
    print(lengths)  # {65536, 8192}
    print(offsets)  # {0, 8192, 123456, 1945251, 1937059, 2002595, 131648, 654321, 662513}


def get_all_length_values():
    pass


if __name__ == '__main__':
    get_all_possible_operations()