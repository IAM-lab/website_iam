import urllib.request
from pathlib import Path
import subprocess
import time

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.customization import convert_to_unicode

path = "bibliography/dblp-ids.txt"
ignore_files_from_dblp = []
with  open(path,'r') as file:
    file_name = 0
    for line in file.read().splitlines() :
        id, author = line.split("|")
        file_name += 1
        bib =  f'bibliography/bib/{file_name}.bib'
        urllib.request.urlretrieve(id, bib)

        # Ignore entries of procedings used by crossref fields
        db = BibDatabase()
        db.entries = []
        with open(bib, 'r', encoding='utf-8') as bibtex_file:
                parser = BibTexParser(common_strings=True)
                bib_database = bibtexparser.load(bibtex_file, parser=parser)
                for entry in bib_database.entries:
                    if author in str(entry) and not any(bibkey in str(entry) for bibkey in ignore_files_from_dblp):
                        db.entries.append(entry)

        writer = BibTexWriter()
        with open(bib, 'w') as bibfile:
            bibfile.write(writer.write(db))

for bib in Path("bibliography/bib/").glob("*.bib"):
    subprocess.call(f'academic import --bibtex {bib}', shell = True)
