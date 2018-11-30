#!/usr/bin/python
# convert yong format to rime format
import sys

def parse_line(line):
    fields = line.split()
    code = fields[0]
    phrases = []
    for phrase in fields[1:]:
        phrases.append((code, phrase))
    return phrases

def main():
    src_file_name = sys.argv[1]
    dst_file_name = sys.argv[2]
    find_data = False

    try:
        src_fp = open(src_file_name) 
        dst_fp = open(dst_file_name, 'w')
        while True:
            line = src_fp.readline()
            if not line:
                break
            if not find_data:
                # skip lines before [data]
                if line.startswith('[data]'):
                    find_data = True
                continue
            phrases = parse_line(line)
            for phrase in phrases:
                dst_fp.write('%s\t%s\n' % (phrase[1], phrase[0]))
    finally:
        src_fp.close()
        dst_fp.close()
    

if __name__ == '__main__':
    main() 
