
from tracker.models import RequestLogs


# Middleware to log each incoming HTTP request.
# Stores request method, path, and raw request data using vars(request).
# Note: vars(request) may include non-serializable data — use request.META for safety.
# Prints the response (for debugging); avoid in production.



class RequestLogging:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        RequestLogs.objects.create(
            request_info = vars(request),
            request_type = request.method,
            request_method = request.path
        )
        return self.get_response(request)
        