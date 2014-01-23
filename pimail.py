import web
import json
from jinja2 import Template
import random

" Load Data "
with open("data.json") as f:
    meps = json.load(f)

class mail:
    """ Handle Requests for Mail """
    def GET(self):
        """ Handle GET Requests """
        web.header("Content-Type", "text/html;charset=utf-8")
        with open("widget.tmpl") as f:
            template = Template(f.read().decode("utf-8"))
        m = random.choice(meps)
        return template.render(m)

urls = ('/', 'mail' )

app = web.application(urls,globals())

if __name__ == "__main__":
    app.run()
