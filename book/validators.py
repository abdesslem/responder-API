import functools
import json

try:
    import jsonschema
except ImportError:
    pass


def validate(schema):
    """Decorator for validating ``req.media`` using JSON Schema.

    This decorator provides standard JSON Schema validation via the
    ``jsonschema`` package available from PyPI.

    Args:
        schema (dict): A dictionary that follows the JSON Schema specification.
            See `json-schema.org <http://json-schema.org/>`_ for more
            information on defining a compatible dictionary.

    Example:
        .. code:: python

            from validators import validate

            # -- snip --

            @validate(my_post_schema)
            def on_post(self, req, resp):

            # -- snip --

    """

    def decorator(func):
        @functools.wraps(func)
        async def wrapper(self, req, resp, *args, **kwargs):
            try:
                jsonschema.validate(json.loads(await req.text), schema)
                return await func(self, req, resp, *args, **kwargs)
            except jsonschema.ValidationError as e:
                resp.media = {
                    "message": "You have to provide a valid json schema"
                }

        return wrapper
    return decorator