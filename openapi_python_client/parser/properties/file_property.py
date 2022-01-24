from .property import Property
import attr
from typing import ClassVar, Set

@attr.s(auto_attribs=True, frozen=True)
class FileProperty(Property):
    """A property used for uploading files"""

    _type_string: ClassVar[str] = "File"
    # Return type of File.to_tuple()
    _json_type_string: ClassVar[str] = "Tuple[Optional[str], Union[BinaryIO, TextIO], Optional[str]]"
    template: ClassVar[str] = "file_property.py.jinja"

    def get_imports(self, *, prefix: str) -> Set[str]:
        """
        Get a set of import strings that should be included when this property is used somewhere

        Args:
            prefix: A prefix to put before any relative (local) module names. This should be the number of . to get
            back to the root of the generated client.
        """
        imports = super().get_imports(prefix=prefix)
        imports.update({f"from {prefix}types import File", "from io import BytesIO"})
        return imports

