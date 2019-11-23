

def main():
    structure = {}
    section_line_idx = False
    chapter_line_idx = False
    current_section = None
    current_chapter = None

    with open('notes.html', 'r') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            if '<div class="sectionHeading">' in line:
                section_line_idx = idx + 1
                continue

            if idx and idx == section_line_idx:
                current_section = line.strip().capitalize()
                structure[current_section] = {}
                continue

            if '<div class="noteHeading">' in line:
                chapter_line_idx = idx + 1
                continue

            if idx and idx == chapter_line_idx:
                chapter = line.split(') -')[1].split('>')[0]
                chapter = chapter.strip().split()
                chapter[1] = f'{chapter[1]}.'
                chapter[0] = chapter[0].capitalize()
                chapter[2] = chapter[2].capitalize()
                current_chapter = ' '.join(chapter)
                if current_chapter not in structure[current_section]:
                    structure[current_section][current_chapter] = []
                continue

            if '<div class="noteText">' in line:
                note = lines[idx + 1].replace('\n', '')
                structure[current_section][current_chapter].append(note)

    for section, chapters in structure.items():
        print(section)
        for chapter, texts in chapters.items():
            print(chapter)
            print(*texts, sep='\n')

if __name__ == '__main__':
    main()
