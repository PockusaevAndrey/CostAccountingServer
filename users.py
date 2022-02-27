import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.options
import tornado.web
from tornado.options import define, options

from servers.users.UserServer import UserServer

define("port", default=8888, help="run on the given port", type=int)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(UserServer())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
