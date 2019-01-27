from flask_api import status

from api.models import User
from api.schemas.user import UserSchema

user_schema = UserSchema()

def get_users(request_args=None):
    result = User.query.filter_by(**request_args.to_dict())
    return user_schema.jsonify(result)

def get_user_by_id(id, request_args=None):
    # result = User.get(id, **request_args.to_dict())
    result = User.query.get(1)
    return user_schema.jsonify(result)

def post_user(request_args=None):
    pass
#     try:
#         user = User(**request_args.to_dict())
#         result = user.save()
#         return result.to_json(), status.HTTP_200_OK
#     except ValidationError as e:
#         return str(e), status.HTTP_400_BAD_REQUEST
