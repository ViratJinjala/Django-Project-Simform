from django.http import JsonResponse
import json

class EmailDomainValidatorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.trusted_domains = ["gmail.com", "microsoft.com", "outlook.com"]

    def __call__(self, request):
        # Only target the specific endpoint
        if request.path == "/api/users/create/" and request.method == "POST":
            try:
                # Get body data safely
                if request.content_type == "application/json":
                    data = json.loads(request.body)
                    email = data.get("email", "")
                else:
                    # For form data
                    email = request.POST.get("email", "")
                
                # Extract domain
                domain = email.split('@')[-1]

                # Validate domain
                if domain not in self.trusted_domains:
                    return JsonResponse({
                        "success": False,
                        "message": f"Email domain '{domain}' is not allowed."
                    }, status=403)

            except Exception as e:
                return JsonResponse({
                    "success": False,
                    "message": "Invalid email format or request body.",
                    "error": str(e)
                }, status=400)

        # Allow request to proceed
        return self.get_response(request)
