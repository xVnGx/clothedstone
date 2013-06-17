class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('This is the HomeHandler.')

class ProductListHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('This is the ProductListHandler.')

class ProductHandler(webapp2.RequestHandler):
    def get(self, product_id):
        self.response.write('This is the ProductHandler. '
            'The product id is %s' % product_id)

app = webapp2.WSGIApplication([
    (r'/', HomeHandler),
    (r'/products', ProductListHandler),
    (r'/products/(\d+)', ProductHandler),
])