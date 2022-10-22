import asyncio

import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Azul, Algeria !!!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(8080)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
