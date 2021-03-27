from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HTTPValidationError")


@attr.s(auto_attribs=True)
class HTTPValidationError:
    """  """

    detail: Union[Unset, List[None]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        detail: Union[Unset, List[None]] = UNSET
        if not isinstance(self.detail, Unset):
            detail = []
            for detail_item_data in self.detail:
                detail_item = None

                detail.append(detail_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        detail = []
        _detail = d.pop("detail", UNSET)
        for detail_item_data in _detail or []:
            detail_item = None

            detail.append(detail_item)

        http_validation_error = cls(
            detail=detail,
        )

        return http_validation_error
