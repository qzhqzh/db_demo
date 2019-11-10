from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework.views import exception_handler
import logging
import traceback


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    # if response is not None:
    #     response.data['status_code'] = response.status_code
    logging.getLogger('debug').error(traceback.format_exc())
    if isinstance(exc, ValidationError) and not response:
        return Response(exc.messages, status=400)
    return response