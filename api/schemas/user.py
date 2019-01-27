from api.app import ma
from api.models import User, Gender

class GenderSchema(ma.ModelSchema):
    class Meta:
        model = Gender

class UserSchema(ma.Schema):
    class Meta:
        # model = User
        # gender = ma.Nested(GenderSchema)
        fields = ('id', 'gender')
    gender = dict(id='kim')
