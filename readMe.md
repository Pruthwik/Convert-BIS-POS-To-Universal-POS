# How to run the code
python convert_bis_to_universal_pos_tag.py --input sample-hin-BIS.txt --map bis_to_ud.json --output sample-hin-universal.txt

# input file should be in conll format, each line is of the format "token\tBIS-tag" and lines are separated by a blank line.
# bis_to_ud contains the mapping from BIS to Universal POS tagset
# output file will be generated in the same format "token\tUniversal-tag" and lines are separated by a blank line.
