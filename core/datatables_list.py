from controls.datatables import PydanticDatatable
from pydantic_models.datatables import User, UserResponse


class UsersTable(PydanticDatatable):
    url = '/admin/users/'
    table_pydantic_model = User
    table_response_model = UserResponse
