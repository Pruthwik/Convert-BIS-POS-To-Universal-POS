"""Convert BIS to Universal POS Tag."""
from argparse import ArgumentParser
from json import load
from re import search


def read_conll_file(file_path):
    '''
    :param file_path: Path of the Feature File
    :return Lines: Lines read from the feature file
    '''
    with open(file_path, 'r', encoding='utf-8') as finp:
        return finp.readlines()


def convert_bis_tags_to_universal(lines, mapping):
    '''
    :param lines: Lines read from the feature file
    :param mapping: Dictionary containig mapping from BIS to UT (Universal Tagset)
    :return changed_lines: Returns list of lines after changing the tags
    '''
    changed_lines = list()
    for line in lines:
        line = line.strip()
        if line:
            token, tag = line.split('\t')
            changed_tag = ''
            for key in mapping:
                if search(key, tag):
                    changed_tag = mapping[key]
                    changed_lines.append(token + '\t' + changed_tag)
                    break
            if not changed_tag:
                changed_tag = 'X'
                changed_lines.append(token + '\t' + changed_tag)
        else:
            changed_lines.append('')
    return changed_lines


def write_lines_to_file(out_path, lines):
    '''
    :param outpath: File path of the output file
    :param lines: Lines to be written into the file
    :return: None
    '''
    with open(out_path, 'w', encoding='utf-8') as fout:
        fout.write('\n'.join(lines) + '\n')


def read_json_file(file_path):
    '''
    :param file_path: Path of the JSON file containing the mapping
    :return mapping: Returns the mapping between the tagsets
    '''
    mapping = load(open(file_path, 'r', encoding='utf-8'))
    return mapping


def main():
    """Pass arguments and call functions here."""
    parser = ArgumentParser()
    parser.add_argument('--input', dest='inp', help='Enter the input file path')
    parser.add_argument('--map', dest='map', help='Enter the mapping file path')
    parser.add_argument('--output', dest='out', help='Enter the output file path')
    args = parser.parse_args()
    lines = read_conll_file(args.inp)
    mapping = read_json_file(args.map)
    changed_lines = convert_bis_tags_to_universal(lines, mapping)
    write_lines_to_file(args.out, changed_lines)


if __name__ == '__main__':
    main()
