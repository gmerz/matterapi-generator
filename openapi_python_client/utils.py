import builtins
import re
from keyword import iskeyword

import stringcase


def sanitize(value: str) -> str:
    """ Removes every character that isn't 0-9, A-Z, a-z, ' ', -, or _ """
    return re.sub(r"[^\w _\-]+", "", value)


def fix_keywords(value: str) -> str:
    if iskeyword(value):
        return f"{value}_"
    return value


RESERVED_WORDS = set(dir(builtins)).union({"self"})


def fix_reserved_words(value: str) -> str:
    #if value in RESERVED_WORDS:
    #    return f"{value}_"
    return value


def group_title(value: str) -> str:
    value = re.sub(r"([A-Z]{2,})([A-Z][a-z]|[ \-_]|$)", lambda m: m.group(1).title() + m.group(2), value.strip())
    value = re.sub('(^|[ _-]+|[a-z]+)([A-Z])([A-Z][a-z])', lambda m: m.group(1) + m.group(2) + m.group(3).lower(), value)
    value = re.sub(r"(^|[ _-])([A-Z])", lambda m: m.group(1) + m.group(2).lower(), value)
    return value


def snake_case(value: str) -> str:
    return fix_keywords(stringcase.snakecase(group_title(sanitize(value))))


def pascal_case(value: str) -> str:
    return fix_keywords(stringcase.pascalcase(sanitize(value.replace(" ", ""))))


def kebab_case(value: str) -> str:
    return fix_keywords(stringcase.spinalcase(group_title(sanitize(value))))


def remove_string_escapes(value: str) -> str:
    return value.replace('"', r"\"")


# This can be changed by config.Config.load_config
FIELD_PREFIX = "field_"


def to_valid_python_identifier(value: str) -> str:
    """
    Given a string, attempt to coerce it into a valid Python identifier by stripping out invalid characters and, if
    necessary, prepending a prefix.

    See:
        https://docs.python.org/3/reference/lexical_analysis.html#identifiers
    """
    new_value = fix_reserved_words(fix_keywords(sanitize(value)))

    if new_value.isidentifier():
        return new_value

    return f"{FIELD_PREFIX}{new_value}"


def clean_description(description):
    if not description:
        return description
    regex_perm = '#+\s*Permissions\s+(\S[^\n]+)\n'
    regex_version = '__Minimum server version_*: ([^_\s]*)_*\s'
    regex_local = '__Local mode only_*:_*:* ([^\n]*)_*\n'
    regex_note = '__Note_*:_*:* ([^\n]*)_*\n'
    repl_perms = re.findall(regex_perm, description)
    repl_version = re.findall(regex_version, description)
    repl_note = re.findall(regex_note, description)
    repl_local = re.findall(regex_local, description)
    description = re.sub(regex_perm,"", description,flags=re.S)
    description = re.sub(regex_version,"", description,flags=re.S)
    description = re.sub(regex_note,"", description,flags=re.S)
    description = re.sub(regex_local,"", description,flags=re.S)
    description = re.sub("\n\n+","\n\n", description,flags=re.S)
    description.replace('`', '``')
    description = description.strip()

    if repl_perms or repl_version or regex_local or repl_note:
        description += '\n'

    if repl_perms:
        description += f'\nPermissions:\n    {repl_perms[0]}'
    if repl_version:
        description += f'\nMinimum Server Version:\n    {repl_version[0]}'
    if repl_local:
        description += f'\nLocal Mode Only:\n    {repl_local[0]}'
    # Additional newline before warning to make sphinx happy
    if repl_note:
        description += f'\n\nWarning:\n    {repl_note[0]}'
    
    return description



