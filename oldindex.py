import cherrypy
import os

curdir = os.path.dirname(os.path.abspath(__file__))
class index(object):

    @cherrypy.expose()
    def index(self):
        return "Hello World"

if __name__=='__main__':
    cherrypy.quickstart(index())