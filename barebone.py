import webapp2

form="""

"""

class MainPage(webapp2.RequestHandler):
  # def get(self):
    # self.response.out.write(form)

  def post():
    self.request.out.write(form)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)