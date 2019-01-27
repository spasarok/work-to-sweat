from api.app import ma
from api.models import User, Gender

class GenderSchema(ma.ModelSchema):
    class Meta:
        model = Gender

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        gender_id = ma.Nested(GenderSchema)

    # @ma.pre_load
    # def slugify_name(self, in_data):
    #     in_data['slug'] = in_data['slug'].lower().strip().replace(' ', '-')
    #     return in_data
