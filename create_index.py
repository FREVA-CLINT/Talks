"""Create a new index.html for display at gitlab pages."""

from pathlib import Path
import shutil

HEADER = """<!DOCTYPE html>
<html>
<head>
<style>
h1 {{text-align: center;}}
p {{text-align: center;}}
div {{text-align: center;}}
</style>
</head>
<body>

<h1>Select a presentation:</h1>
<div>
{links}
</div>
</body>
</html>
"""

LINK_TMPL = '<a href="{href}">{name}</a><br><br>'

if __name__ == "__main__":
    talk_dir = Path(__file__).parent / "talks"
    public_dir = Path(__file__).parent / "public"
    links = []
    try:
        shutil.rmtree(public_dir)
    except FileNotFoundError:
        pass
    public_dir.mkdir(exist_ok=True, parents=True)
    for _dir in talk_dir.iterdir():
        shutil.copytree(_dir, public_dir / _dir.name)
        link = Path(_dir.name) / "index.slides.html"
        name = " ".join(_dir.name.split("_"))
        links.append(LINK_TMPL.format(href=link, name=name))
    with (public_dir / "index.html").open("w") as fo_obj:
        fo_obj.write(HEADER.format(links="\n".join(links)))
