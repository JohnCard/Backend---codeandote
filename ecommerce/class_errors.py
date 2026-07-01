from rest_framework.exceptions import APIException

class MiError(APIException):
    status_code = 418
    default_detail = 'Error personalizado'
    default_code = 'mi_error'

# uso
# raise MiError("Más detalle aquí")