from rest_framework.response import Response

def custom_api_response(success=True, message="", data=None, status_code=200):
    """
    یک تابع عمومی برای یکپارچه کردن خروجی تمام APIهای پروژه.
    """
    response_data = {
        "success": success,
        "message": message,
        "data": data if data is not None else {}
    }
    return Response(response_data, status=status_code)