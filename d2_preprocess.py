import sys

class StyleBlock:
    def __init__(self):
        self.lines = []

    def append(self, line):
        self.lines.append(line)

    def is_empty(self):
        return len(self.lines) == 0

    def clear(self):
        self.lines = []

    def get(self):
        return self.lines

    def __str__(self):
        return ''.join(self.lines)

    def __repr__(self):
        return self.__str__()
    
    def serialize(self):
        return "style: {\n" + self.__str__() + "}\n"


def remove_empty_style_blocks(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    inside_style_block = False
    style_block = StyleBlock()

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('style:'):
            inside_style_block = True
            style_block.clear()
            continue

        if stripped_line.startswith('}') and inside_style_block:
            inside_style_block = False
            if style_block.is_empty() is False:
                modified_lines.append(style_block.serialize())
            continue
            
        if inside_style_block:
            style_block.append(line)
            continue
        
        modified_lines.append(line)

    with open(filename, 'w') as file:
        file.writelines(modified_lines)

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 d2_preprocess.py <filename>')
        return

    filename = sys.argv[1]
    remove_empty_style_blocks(filename)

if __name__ == '__main__':
    main()