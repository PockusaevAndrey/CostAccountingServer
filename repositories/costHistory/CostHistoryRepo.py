from repositories.costHistory.CostHistoryEntity import CostHistoryEntity, IncompleteCostHistory


class CostHistoryRepo:
    """Repository for CostHistoryServer"""

    def add(self, cell: CostHistoryEntity) -> None:
        pass

    def get(self) -> list[IncompleteCostHistory]:
        pass

    def update(self, cell: CostHistoryEntity) -> None:
        pass

    def info(self, cell: IncompleteCostHistory) -> CostHistoryEntity:
        pass
