from pydantic import BaseModel


class IncompleteCostHistory(BaseModel):
    pass


class CostHistoryEntity(IncompleteCostHistory):
    pass
