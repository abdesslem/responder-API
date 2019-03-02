import responder
import time
import json

from book.model import books, book_post_schema
from book.validators import validate

api = responder.API()


@api.route("/books")
class Book():
    async def on_get(self, req, resp):
        resp.media = books

    @validate(book_post_schema)
    async def on_post(self, req, resp):
        new_book = json.loads(await req.text)
        try:
            books.append(new_book)
            resp.media = new_book
        except:
            resp.media = {"message": "An Error occured"}


# If you want your API to send back JSON, 
# simply set the resp.media property to a JSON-serializable Python object


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
