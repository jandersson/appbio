def is_match(field, alignment):
    if field in alignment.hit_def:
        return True
    if field in alignment.hit_id:
        return True
    if field in alignment.accession:
        return True
    return False

def update_min(data, query, hit_def, bits, expect):
    if hit_def not in data:
        data[hit_def] = {'bits': bits, 'expect': expect, 'query': query}
    elif data[hit_def]['expect'] > expect:
        data[hit_def] = {'bits': bits, 'expect': expect, 'query': query}
    return data
    

if __name__ == '__main__':
    from common import is_valid_file
    import argparse
    from Bio.Blast import NCBIXML
    import re

    parser = argparse.ArgumentParser(description='Parse Blast Query Result XML file')
    parser.add_argument('field', help='Field to search in the blast hit list')
    parser.add_argument('file', type=lambda f: is_valid_file(f, parser), help='XML file to parse')
    args = parser.parse_args()

    E_THRESH = 1e-20
    fd = open(args.file)
    data = {}
    output_string = "{:<10}{:<15}{:<10}{}"
    result = NCBIXML.parse(fd)
    for record in result:
        for alignment in record.alignments:
            if is_match(args.field, alignment):
                for hsp in alignment.hsps:
                    if hsp.expect < E_THRESH:
                        update_min(data, record.query, re.search('(?<=\|)\w+', alignment.hit_def).group(0), hsp.bits, hsp.expect)
    for k, v in data.items():
        print(
            output_string.format(
                v['query'], k, v['bits'], v['expect']
            )
        )