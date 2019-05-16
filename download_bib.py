import urllib.request
from pathlib import Path
import subprocess
import time

path = "bibliography/dblp-ids.txt"
with  open(path,'r') as file:
    file_name = 1
    for id in file.readlines():
        urllib.request.urlretrieve(id, f'bibliography/bib/{file_name}.bib')
        file_name += 1
        time.sleep(7) # Pause to avoid dblp injecting random papers

for bib in Path("bibliography/bib/").glob("*.bib"):
    subprocess.call(f'academic import --bibtex {bib}', shell = True)
