# exceptions.py

import logging
import traceback

from rest_framework.response import Response
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def system_general_exception_handler(exc, context):
    # Call DRF's default exception handler first to get the standard error response.
    response = exception_handler(exc, context)

    if response is None:
        # If DRF's exception handler didn't handle the exception, it means it's an unhandled exception.
        # Log the exception for debugging purposes.
        traceback_str = traceback.format_exc()
        logger.error(f"Unhandled Exception: {traceback_str}")

        # Return a generic error response to the client.
        return Response(
            {"error": "An error occurred while processing the request."},
            status=500,
        )

    return response
