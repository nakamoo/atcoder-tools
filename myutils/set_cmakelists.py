import os
import sys
from jinja2 import Template, Environment, FileSystemLoader
args = sys.argv

contest_id = os.path.split(os.getcwd())[1]
problems = [f.name for f in os.scandir() if f.is_dir()]


env = Environment(loader=FileSystemLoader(args[1]))
template = env.get_template('CMakeLists.tpl.txt')

data = {"contest_id": contest_id, "problems": problems}

rendered = template.render(data)
print(str(rendered))
