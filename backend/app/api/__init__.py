# Team members:
# 1. Anusha Gurram – G01514835
# 2. Bala Naga Tirumala Kiran Annadata – G01508483
# 3. Yashwanth Karthikeya Settem– G01512992

# Defines the main "/api" router and adds the surveys routes under "/api/surveys".


from fastapi import APIRouter

from .surveys import router as surveys_router

api_router = APIRouter(prefix="/api")
api_router.include_router(surveys_router, prefix="/surveys", tags=["surveys"])

__all__ = ["api_router"]

