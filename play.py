import os
import webapp2
import jinja2
import re

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


# Creating a database for the blogposts
# bp = name of db with blogposts
# in bp we have three diffrent colums:
# title = string
# body = text the blogpost itself
# created which is the timestamp colum
class bp(db.Model):
    title = db.StringProperty(required = True)
    body = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

# Rendering the frontpage
class frontpage(Handler):
    def render_front(self, title="", body="", error=""):
        blogposts = db.GqlQuery("select * from bp order by created desc")
        self.render("play.html", title=title, bp=blog, error=error)

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            a = Art(title = title, art = art)
            a.put()
            self.redirect('/')
        else:
            error = "We need a title and some art man!"
            self.render_front(title, art, error)

app = webapp2.WSGIApplication([('/', frontpage)],
                              debug=True)