import webapp2 

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("hello world!")
        a=0
        self.response.write(a)
        self.response.write("<br>")
        b=1
        self.response.write(b)
        self.response.write("<br>")
        for i in range(1,6):
            c=a+b
            a=b
            b=c
            self.response.write(c)

app = webapp2.WSGIApplication(['/',MainPage()],debug=True)