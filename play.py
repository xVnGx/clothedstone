import    webapp2
def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day

def valid_month(month):
     if 

form="""
<form>
     <label>
          Day
          <input type="text" name="day">
     </label>

     <label>
          Month
          <input type="text" name="month">
     </label>

     <label>
          Year
          <input type="text" name="year">
     </label>

<br>
<br>

<input type='submit'>

</form>
"""


class MainPage(webapp2.RequestHandler):
     def get(self):
          self.response.out.write(form)

     def post(self):
          
          user_month = valid_month(self.request.get('month'))
          user_day = valid_day(self.request.get('day'))
          user_year = valid_year(self.request.get('year'))

          if not(user_year and user_day and user_month):
               self.response.out.write(form)
          else:
               self.response.out.write("Thanks, that is totally a valid day!")
          

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

