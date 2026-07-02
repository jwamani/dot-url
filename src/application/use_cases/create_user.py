from src.domain.entities.user import User
from src.application.interfaces import IApiKeyGenRepository, AbstractUnitOfWork, IUserRepository
from src.application.dtos.user_dtos import CreateUserRequest, UserResponse

class CreateUser:
    def __init__(self, uow: AbstractUnitOfWork, api_key_generator: IApiKeyGenRepository) -> None:
        self._uow = uow
        self._api_key_generator = api_key_generator
    
    async def execute(self, request: CreateUserRequest) -> UserResponse:
        api_key = self._api_key_generator.generate()
        user = User(
            email=request.email,
            password=request.password,
            api_key=api_key,
        )
        
        created_user = await self._uow.users.create_user(user)
        await self._uow.commit()
        
        return UserResponse(
            id=created_user.id or 0,
            email=created_user.email,
            api_key=created_user.api_key,
            is_active=created_user.is_active,
            created_at=created_user.created_at.isoformat() ,
            updated_at=created_user.updated_at.isoformat()
        )