from fastapi import APIRouter, Depends, HTTPException, exceptions, status
from fastapi import APIRouter
from src.auth.config import auth_backend, fastapi_users
from src.auth.schemas import UserCreate, UserRead
from src.auth.manager import get_user_manager
from fastapi_users.exceptions import UserAlreadyExists
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/jwt",
    tags=["Auth"])

@router.post("/register", response_model=UserRead)
async def register_new_user(user_create: UserCreate, user_manager=Depends(get_user_manager)):
    try:
        created_user = await user_manager.create(user_create, safe=True)
        return created_user
    except UserAlreadyExists:
        raise HTTPException(status_code=409, detail={
            "status": "error",
            "data": None,
            "details": "This email address is already registered."   
        })
    except Exception as e:
        logger.exception("An error occurred during user registration:")
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": "An error occurred during user registration. Please check the logs for more information."   
        })



router.include_router(
    fastapi_users.get_auth_router(auth_backend)
)

# router.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="",
#     tags=["Auth"],
# )
