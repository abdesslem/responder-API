# A module to get a list of books

books = [
    {
        "id": 1,
        "name": "The art of deception",
        "author": "Mitnick",
        "isbn": 723812622115},
    {
        "id": 2,
        "name": "Design pattern",
        "author": "Richard Helm",
        "isbn": 1723815487566457},
    {
        "id": 3,
        "name": "Design pattern explained",
        "Author": "Alan Shalloway",
        "isbn": 1723815487566457}
]

book_post_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Books",
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "author": {
            "type": "string"
        },
        "isbn": {
            "description": "The ISBN number of the book",
            "type": "string"
        }
  },
  "required": ["name", "author"]
}