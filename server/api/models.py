from pydantic import BaseModel, Field
from typing import Optional, List, Any, Union

class OpportunityValue(BaseModel):
    amount: float = Field(..., description="The monetary amount of the opportunity.")
    currency: str = Field(..., description="The currency code (e.g., 'EUR', 'USD').")

class OpportunityParty(BaseModel):
    id: int = Field(..., description="The unique ID of the main contact (party) for this opportunity.")

class OpportunityMilestone(BaseModel):
    id: int = Field(..., description="The unique ID of the milestone this opportunity belongs to.")

class OpportunityCreate(BaseModel):
    """
    OpportunityCreate Model
    Represents an opportunity to be created in Capsule. For reporting and value queries, the 'current_value' property should be used if present, as it reflects the probability-weighted value of the opportunity.
    The 'value_type' field is required and must be either 'per_unit' (value.amount is per duration unit) or 'total' (value.amount is the total for all units).
    """
    name: str = Field(..., description="The name of this opportunity.")
    party: OpportunityParty = Field(..., description="The main contact (party) for this opportunity.")
    milestone: OpportunityMilestone = Field(..., description="The milestone this opportunity belongs to.")
    value: OpportunityValue = Field(..., description="The value of this opportunity (base amount). For reporting, use 'current_value' if present.")
    value_type: str = Field(..., description="Required. 'per_unit' if value.amount is per duration unit (e.g. per month), 'total' if value.amount is the total for all units.")
    description: Optional[str] = Field(None, description="The description of this opportunity.")
    expectedCloseOn: Optional[str] = Field(None, description="The expected close date (ISO8601) of this opportunity.")
    probability: Optional[int] = Field(None, description="The probability (percentage) of winning this opportunity. Used to calculate 'current_value'.")
    durationBasis: Optional[str] = Field(None, description="The time unit used by the duration field. Accepted values: FIXED, HOUR, DAY, WEEK, MONTH, QUARTER, YEAR.")
    duration: Optional[int] = Field(None, description="The duration of this opportunity. Must be null if durationBasis is FIXED.")
    # Add more fields as needed for full Opportunity model

    @property
    def total_value(self) -> Optional[float]:
        """The total value of the opportunity, considering duration and amount."""
        if self.value and self.value.amount is not None:
            if self.durationBasis and self.durationBasis != "FIXED" and self.duration is not None:
                return self.value.amount * self.duration
            return self.value.amount
        return None

    @property
    def current_value(self) -> Optional[float]:
        """The probability-weighted value of the opportunity. This is the relevant value for reporting and user queries."""
        if self.total_value is not None and self.probability is not None:
            return self.total_value * self.probability / 100
        return None

class Address(BaseModel):
    id: int
    type: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    street: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None

class PhoneNumber(BaseModel):
    id: int
    type: Optional[str] = None
    number: str

class Website(BaseModel):
    id: int
    type: Optional[str] = None
    address: str
    service: Optional[str] = None
    url: Optional[str] = None

class EmailAddress(BaseModel):
    id: int
    type: Optional[str] = None
    address: str

class Organisation(BaseModel):
    id: int = Field(..., description="The unique ID of this organisation.")
    type: str = Field("organisation", description="The type of party. Always 'organisation' for organisations.")
    name: str = Field(..., description="The name of the organisation.")
    about: Optional[str] = Field(None, description="A short description of the organisation.")
    createdAt: Optional[str] = Field(None, description="The ISO date/time when this organisation was created.")
    updatedAt: Optional[str] = Field(None, description="The ISO date/time when this organisation was last updated.")
    lastContactedAt: Optional[str] = Field(None, description="The ISO date/time when this organisation was last contacted.")
    addresses: Optional[List[Address]] = Field(None, description="All addresses associated with this organisation.")
    phoneNumbers: Optional[List[PhoneNumber]] = Field(None, description="All phone numbers associated with this organisation.")
    websites: Optional[List[Website]] = Field(None, description="All websites and social network accounts associated with this organisation.")
    emailAddresses: Optional[List[EmailAddress]] = Field(None, description="All email addresses associated with this organisation.")
    pictureURL: Optional[str] = Field(None, description="URL of the profile picture for this organisation.")
    tags: Optional[List[Any]] = Field(None, description="Tags added to this organisation.")
    fields: Optional[List[Any]] = Field(None, description="Custom fields defined for this organisation.")
    owner: Optional[Any] = Field(None, description="The user this organisation is assigned to.")
    team: Optional[Any] = Field(None, description="The team this organisation is assigned to.")
    missingImportantFields: Optional[bool] = Field(None, description="Indicates if any important custom fields are missing a value.")

class Person(BaseModel):
    id: int = Field(..., description="The unique ID of this person.")
    type: str = Field("person", description="The type of party. Always 'person' for persons.")
    firstName: Optional[str] = Field(None, description="The first name of the person.")
    lastName: Optional[str] = Field(None, description="The last name of the person.")
    title: Optional[str] = Field(None, description="The title of the person.")
    jobTitle: Optional[str] = Field(None, description="The job title of the person.")
    organisation: Optional[Organisation] = Field(None, description="The organisation this person is associated with.")
    about: Optional[str] = Field(None, description="A short description of the person.")
    createdAt: Optional[str] = Field(None, description="The ISO date/time when this person was created.")
    updatedAt: Optional[str] = Field(None, description="The ISO date/time when this person was last updated.")
    lastContactedAt: Optional[str] = Field(None, description="The ISO date/time when this person was last contacted.")
    addresses: Optional[List[Address]] = Field(None, description="All addresses associated with this person.")
    phoneNumbers: Optional[List[PhoneNumber]] = Field(None, description="All phone numbers associated with this person.")
    websites: Optional[List[Website]] = Field(None, description="All websites and social network accounts associated with this person.")
    emailAddresses: Optional[List[EmailAddress]] = Field(None, description="All email addresses associated with this person.")
    pictureURL: Optional[str] = Field(None, description="URL of the profile picture for this person.")
    tags: Optional[List[Any]] = Field(None, description="Tags added to this person.")
    fields: Optional[List[Any]] = Field(None, description="Custom fields defined for this person.")
    owner: Optional[Any] = Field(None, description="The user this person is assigned to.")
    team: Optional[Any] = Field(None, description="The team this person is assigned to.")
    missingImportantFields: Optional[bool] = Field(None, description="Indicates if any important custom fields are missing a value.")

Party = Union[Person, Organisation]

class Pipeline(BaseModel):
    id: int
    name: str

class Milestone(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    complete: Optional[bool] = None
    probability: int
    pipeline: Optional[Pipeline] = None
    daysUntilStale: Optional[int] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None 

class Category(BaseModel):
    id: int = Field(..., description="The unique ID of the task category.")
    name: str = Field(..., description="The name of the task category.")
    colour: Optional[str] = Field(None, description="The color code of the task category.")

class Repeat(BaseModel):
    interval: Optional[int] = Field(None, description="How often this task repeats (e.g. every interval week/months).")
    frequency: Optional[str] = Field(None, description="If this task repeats every week, month or year. YEARLY, MONTHLY, WEEKLY.")
    on: Optional[str] = Field(None, description="The day of the week or month this task repeats on. -1 for last day of month.")

class NestedUser(BaseModel):
    id: int = Field(..., description="The unique ID of the user.")
    username: Optional[str] = Field(None, description="The username of the user.")
    name: Optional[str] = Field(None, description="The full name of the user.")

class Task(BaseModel):
    id: int = Field(..., description="The unique ID of this task.")
    category: Optional[Category] = Field(None, description="The category of this task.")
    description: str = Field(..., description="A short description of the task.")
    detail: Optional[str] = Field(None, description="More details about the task.")
    dueTime: Optional[str] = Field(None, description="The time (without a date element) when this task is due (user's timezone).")
    status: Optional[str] = Field(None, description="Status: open, completed, or pending.")
    party: Optional[Party] = Field(None, description="The party this task is linked to.")
    opportunity: Optional[Any] = Field(None, description="The opportunity this task is linked to.")
    owner: Optional[NestedUser] = Field(None, description="The user this task is assigned to.")
    daysAfter: Optional[int] = Field(None, description="Number of days after previous task (if part of a track).")
    taskDelayRule: Optional[str] = Field(None, description="How the due date is calculated for tracks: TRACK_START, END_DATE, LAST_TASK.")
    nextTask: Optional[Any] = Field(None, description="The next task in the track.")
    createdAt: Optional[str] = Field(None, description="The ISO date/time when this task was created.")
    updatedAt: Optional[str] = Field(None, description="The ISO date/time when this task was last updated.")
    dueOn: Optional[str] = Field(None, description="The date (without a time element) when this task is due.")
    completedBy: Optional[str] = Field(None, description="The username of the user that completed this task.")
    completedAt: Optional[str] = Field(None, description="The ISO date/time when this task was completed.")
    kase: Optional[Any] = Field(None, description="The project this task is linked to.")
    taskDayDelayRule: Optional[str] = Field(None, description="How daysAfter is used for tracks: TRACK_DAYS, TRACK_WORKDAYS, TRACK_WEEKS.")
    repeat: Optional[Repeat] = Field(None, description="Repeat rule for recurring tasks.")
    hasTrack: Optional[bool] = Field(None, description="True if the task is part of a track.")

class Condition(BaseModel):
    field: str = Field(..., description="The field for this condition.")
    operator: str = Field(..., description="The operator for this condition (e.g. is, contains, is after, etc.).")
    value: str = Field(..., description="The value for this condition. Type depends on field/operator.")

class OrderBy(BaseModel):
    field: str = Field(..., description="The field to sort by.")
    direction: str = Field(..., description="Sort direction: ascending or descending.")

class Filter(BaseModel):
    conditions: List[Condition] = Field(..., description="An array of individual conditions for this filter (AND logic). May contain nested groups for OR logic.")
    orderBy: Optional[List[OrderBy]] = Field(None, description="Sort order for the results returned by the query.") 