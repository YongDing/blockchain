import tornado.ioloop
import tornado.web
import os
import tornado.autoreload

class BscTokenListHandler(tornado.web.RequestHandler):
    def get(self):
        a = {"a":"b"}
        self.write(a)

def make_app():
    return tornado.web.Application([
        (r"/bsctokens", BscTokenListHandler),
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static/'})
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(21234)

    tornado.autoreload.start()
    for dir, _, files in os.walk('static'):
        [tornado.autoreload.watch(dir + '/' + f) for f in files if not f.startswith('.')]
    tornado.ioloop.IOLoop.current().start()