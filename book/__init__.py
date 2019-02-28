import responder
import time

from book.model import books

api = responder.API()


# If you want your API to send back JSON, 
# simply set the resp.media property to a JSON-serializable Python object

@api.route("/books")
class Book():
    def on_get(self, req, resp):
        resp.media = books
    def on_post(self, req, resp):
        new_book = req.content()
        print(dir(new_book))
        try:
            books.append(new_book)
            resp.media = books
        except:
            resp.media = {"message": "An Error occured"}


@api.route("/books/{id}")
def get_book(req, resp, *, id):
    try:
        resp.media = [book for book in books if book['id'] == int(id)][0]
    except:
        resp.status_code = api.status_codes.HTTP_404
        resp.media = {"message": "Not Found"}

@api.route("/sendmail")
async def sendmail(req, resp):

    @api.background.task
    def process_data(data):
        """Just sleeps for three seconds, as a demo."""
        time.sleep(5)


    # Parse the incoming data as form-encoded.
    # Note: 'json' and 'yaml' formats are also automatically supported.
    data = await req.media()

    # Process the data (in the background).
    process_data(data)

    # Immediately respond that upload was successful.
    resp.media = {'success': True}
