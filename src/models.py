from enum import Enum
from pydantic import BaseModel, Field

class LegalStatus(str, Enum):
    """Enumeration for legal status options"""
    LEGAL = "legal"
    ILLEGAL = "illegal"
    PRESCRIPTION = "prescription-only"
    UNKNOWN = "unknown"

class Availability(str, Enum):
    """Enumeration for availability options"""
    EASILY_AVAILABLE = "easily available"
    RESTRICTED = "restricted"
    NOT_AVAILABLE = "not available"
    UNKNOWN = "unknown"

class DrugInfo(BaseModel):
    """Schema for drug information response"""
    legal_status: LegalStatus = Field(
        description="Legal status of the drug (legal/illegal/prescription-only/unknown)"
    )
    availability: Availability = Field(
        description="Availability status (easily available/restricted/not available/unknown)"
    )
    prescription_requirements: str = Field(
        description="Requirements for obtaining a prescription"
    )
    regulations: str = Field(
        description="Specific regulations or restrictions"
    ) 