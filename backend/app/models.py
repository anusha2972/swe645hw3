# Team members:
# 1. Anusha Gurram – G01514835
# 2. Bala Naga Tirumala Kiran Annadata – G01508483
# 3. Yashwanth Karthikeya Settem– G01512992

# Defines the data models for student surveys using SQLModel, including enums for specific fields and Pydantic models for create, read, and update operations.



from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import EmailStr, field_validator
from sqlalchemy import Column
from sqlalchemy.types import JSON
from sqlmodel import Field, SQLModel


class LikedMostOption(str, Enum):
    STUDENTS = "students"
    LOCATION = "location"
    CAMPUS = "campus"
    ATMOSPHERE = "atmosphere"
    DORM_ROOMS = "dorm_rooms"
    SPORTS = "sports"


class InterestSource(str, Enum):
    FRIENDS = "friends"
    TELEVISION = "television"
    INTERNET = "internet"
    OTHER = "other"


class RecommendationLikelihood(str, Enum):
    VERY_LIKELY = "very_likely"
    LIKELY = "likely"
    UNLIKELY = "unlikely"


class SurveyBase(SQLModel):
    first_name: str = Field(index=True, min_length=1)
    last_name: str = Field(index=True, min_length=1)
    street_address: str = Field(min_length=1)
    city: str = Field(min_length=1)
    state: str = Field(min_length=2, max_length=2)
    zip_code: str = Field(min_length=5, max_length=10)
    phone: str = Field(min_length=7, max_length=20)
    email: str = Field(index=True, max_length=255)
    date_of_survey: date
    liked_most: list[LikedMostOption] = Field(
        default_factory=list,
        sa_column=Column(JSON),
        description="Aspects of campus they liked most (multi-select).",
    )
    interest_source: InterestSource = Field(description="How the student became interested.")
    recommendation_likelihood: RecommendationLikelihood
    additional_comments: Optional[str] = Field(default=None, max_length=1000)

   

class Survey(SurveyBase, table=True):
    __tablename__: str = "student_surveys"

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class SurveyCreate(SurveyBase):
    pass


class SurveyRead(SurveyBase):
    id: int
    created_at: datetime
    updated_at: datetime


class SurveyUpdate(SQLModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    street_address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = Field(default=None, min_length=2, max_length=2)
    zip_code: Optional[str] = Field(default=None, min_length=5, max_length=10)
    phone: Optional[str] = Field(default=None, min_length=7, max_length=20)
    email: Optional[str] = None
    date_of_survey: Optional[date] = None
    liked_most: Optional[list[LikedMostOption]] = None
    interest_source: Optional[InterestSource] = None
    recommendation_likelihood: Optional[RecommendationLikelihood] = None
    additional_comments: Optional[str] = Field(default=None, max_length=1000)

    @field_validator("state", mode="before")
    @classmethod
    def normalize_state(cls, value: Optional[str]) -> Optional[str]:
        if isinstance(value, str):
            return value.upper()
        return value

    
