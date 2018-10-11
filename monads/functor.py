from __future__ import annotations
from typing import Any, Callable, Generic, TypeVar

T = TypeVar("T")
S = TypeVar("S")


class Functor(Generic[T]):
    def fmap(self, function: Callable[[T], S]) -> Functor[S]:
        raise NotImplementedError