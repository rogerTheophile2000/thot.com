import logging
import time

logger = logging.getLogger("django.request")

class RequestLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start = time.time()

        response = self.get_response(request)

        duration = time.time() - start

        user = request.user if request.user.is_authenticated else "Anonymous"

        logger.info(
            f"{request.method} {request.path} "
            f"Status={response.status_code} "
            f"User={user} "
            f"Duration={duration:.3f}s"
        )

        return response



