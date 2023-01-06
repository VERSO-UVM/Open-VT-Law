

import json

def parse_statutes(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    statutes = {}
    current_title = None
    current_chapter = None
    current_subchapter = None
    current_text = []
    for line in lines:
        if line.startswith('Title '):
            if current_title is not None:
                statutes[current_title][current_chapter][current_subchapter] = ' '.join(current_text)
                current_text = []
            current_title = line.strip()
            statutes[current_title] = {}
            current_chapter = None
            current_subchapter = None
        elif line.startswith('Chapter '):
            if current_chapter is not None:
                statutes[current_title][current_chapter][current_subchapter] = ' '.join(current_text)
                current_text = []
            current_chapter = line.strip()
            statutes[current_title][current_chapter] = {}
            current_subchapter = None
        elif line.startswith('Subchapter '):
            if current_subchapter is not None:
                statutes[current_title][current_chapter][current_subchapter] = ' '.join(current_text)
                current_text = []
            current_subchapter = line.strip()
        else:
            current_text.append(line.strip())
    if current_title is not None:
        statutes[current_title][current_chapter][current_subchapter] = ' '.join(current_text)
    return statutes

def write_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def main(filepath):
    statutes = parse_statutes(filepath)
    write_json(statutes, '/Users/kfortney/Desktop/revised.json')

if __name__ == '__main__':
    main('/Users/kfortney/Desktop/law.txt')