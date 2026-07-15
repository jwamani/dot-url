from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.user_repository import IUserRepository
from src.domain.entities.user import User
from src.infrastructure.models.user import User as UserModel


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_user(self, user: User) -> User:
        model = UserModel(
            email=user.email,
            password=user.password,
            api_key=user.api_key_hash,
            is_active=user.is_active,
        )
        self._session.add(model)
        await self._session.flush()
        return User(
            id=str(model.id),
            email=model.email,
            password=model.password,
            api_key_hash=model.api_key_hash,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    async def get_user_by_email(self, email: str) -> User | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        model = result.scalar_one_or_none()
        if model is None:
            return None
        return User(
            id=str(model.id),
            email=model.email,
            password=model.password,
            api_key_hash=model.api_key_hash,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    async def get_user_by_id(self, user_id: int) -> User | None:
        model = await self._session.get(UserModel, user_id)
        if model is None:
            return None
        return User(
            id=str(model.id),
            email=model.email,
            password=model.password,
            api_key_hash=model.api_key_hash,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )
    # TODO: fix this method to verify the hash
    async def get_user_by_api_key(self, api_key: str) -> User | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.api_key_hash == api_key)
        )
        model = result.scalar_one_or_none()
        if model is None:
            return None
        return User(
            id=str(model.id),
            email=model.email,
            password=model.password,
            api_key_hash=model.api_key_hash,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    async def update_user(self, user: User) -> User:
        model = await self._session.get(UserModel, user.id)
        if model is None:
            raise ValueError(f"User {user.id} not found")
        model.email = user.email
        model.password = user.password
        model.api_key_hash = user.api_key_hash
        model.is_active = user.is_active
        await self._session.flush()
        return User(
            id=str(model.id),
            email=model.email,
            password=model.password,
            api_key_hash=model.api_key_hash,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    async def get_all(self) -> list[User]:
        result = await self._session.execute(select(UserModel))
        models = result.scalars().all()
        return [
            User(
                id=str(m.id),
                email=m.email,
                password=m.password,
                api_key_hash=m.api_key_hash,
                is_active=m.is_active,
                created_at=m.created_at,
                updated_at=m.updated_at,
            )
            for m in models
        ]
