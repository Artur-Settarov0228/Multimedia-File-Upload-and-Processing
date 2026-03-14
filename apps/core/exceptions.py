from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    """
    Custom exception handler
    """
    response = exception_handler(exc, context)
    
    if response is None:
        if isinstance(exc, ValidationError):
            data = {
                'error': 'Validation error',
                'details': exc.message_dict if hasattr(exc, 'message_dict') else str(exc)
            }
            response = Response(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Noma'lum xatolik
            logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
            data = {
                'error': 'Internal server error',
                'message': 'Something went wrong'
            }
            response = Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return response