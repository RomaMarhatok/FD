from typing import Generic, TypeVar
from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def get(self, reference: str):
        raise NotImplementedError

    @abstractmethod
    async def add(self, model):
        raise NotImplementedError

    @abstractmethod
    async def list(self, model):
        raise NotImplementedError
