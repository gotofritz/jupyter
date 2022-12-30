import json
import re
from pathlib import Path
from shutil import copy2 as copy
from subprocess import run

root_dir = "katas/"
notebook_glob = "**/solutions/**/*.*"
re_exclude = re.compile(r"/\.")
files = list(
    filter(
        lambda pth: not re_exclude.search(pth.as_posix()),
        Path(root_dir).glob(notebook_glob),
    )
)

re_dest = re.compile(r"/solutions")
for file in files:
    source = file.as_posix()
    dest = re_dest.sub("", source)
    if file.suffix == ".ipynb":
        print("------------- notebook -->")
        print(source)
        print(dest)
        with open(source, "r") as fp:
            src_notebook = json.load(fp)

        for i, cell in enumerate(src_notebook["cells"]):
            try:
                where = cell["source"].index("# solution\n")
                src_notebook["cells"][i]["source"] = cell["source"][: where + 1]
            except ValueError:
                ...

        with open(dest, "w") as fp:
            json.dump(src_notebook, fp)

        try:
            run(["jupyter", "nbconvert", "--execute", "--to", "notebook", "--inplace", dest], text=True, capture_output=True)
            print(output.stdout)
        except BaseException as e:
            print(e)
    else:
        print("------------- asset -->")
        print(source)
        print(dest)
        copy(source, dest)