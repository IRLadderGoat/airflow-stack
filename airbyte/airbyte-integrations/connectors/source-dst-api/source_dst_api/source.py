#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


from abc import ABC
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple

import requests
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from airbyte_cdk.sources.streams.http import HttpStream

# Basic full refresh stream
class DstApiStream(HttpStream, ABC):

    # TODO: Fill in the url base. Required.
    url_base = "https://api.statbank.dk/v1/"

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        return None

    def request_params(self, **kwargs) -> MutableMapping[str, Any]:
        return {}

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        for resp in response.json():
            yield resp


class DstSubjects(DstApiStream):
    primary_key = "id"

    def path(self, **kwargs) -> str:
        return "subjects"

class DstTables(DstApiStream):
    primary_key = "id"

    def path(self, **kwargs) -> str:
        return "tables"

# Source
class SourceDstApi(AbstractSource):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        try:
            resp = requests.get(f"{DstApiStream.url_base}subjects")
            status = resp.status_code
            logger.info(f"Ping response code: {status}")
            if status == 200:
                return True, None
            return False, resp.text
        except Exception as e:
            return False, e

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        return [DstSubjects(), DstTables()]
