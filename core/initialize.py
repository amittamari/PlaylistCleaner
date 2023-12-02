#!/usr/bin/env python3

import regex

from core.types import DATASOURCES_TYPES, AnyDataSource
import datasources

ABSTRACT_INSTANTIATE_ERROR_REGEX = r"(?:Can't instantiate abstract class) (.*DataSource) (?:with abstract method) (.*)"

def initialize_datasources() -> list[AnyDataSource]:
    try:
        initialized_datasources = [
            ds()
            for ds_type_class in DATASOURCES_TYPES
            for ds in ds_type_class.__subclasses__()
        ]

        return initialized_datasources
    except TypeError as e:
        m = regex.match(ABSTRACT_INSTANTIATE_ERROR_REGEX, str(e))
        if m is not None:
            raise NotImplementedError(m.group(1))

        raise e
