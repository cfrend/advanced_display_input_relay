import sys
sys.path.append("/var/www/adr")
import uuid
import re
from dataclasses import dataclass, field
from typing import Dict
from models.model import Model

@dataclass(eq=False)
class adr_Field(Model):
    collection: str = field(init=False, default='adr_fields')
    adr_field: str
    json_data: Dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self):
        return {
            "_id": self._id,
            "adr_field": self.adr_field,
            "json_data": self.json_data
        }

    # Fields should be of the convention "adr_field_###"
    @classmethod
    def get_by_field(cls, adr_field: str) -> "adr_Field":
        return cls.find_one_by("adr_field", adr_field)

    @classmethod
    def get_by_id(cls, adr_id: str) -> "adr_Field":
        return cls.find_one_by("_id", adr_id)
