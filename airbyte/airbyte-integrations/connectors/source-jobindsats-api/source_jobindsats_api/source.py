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
class JobindsatsApiStream(HttpStream, ABC):
    # TODO: Fill in the url base. Required.
    url_base = "https://api.jobindsats.dk/v2/"

    def __init__(self, api_key : str, **kwargs):
        super().__init__(**kwargs)
        self.api_key = api_key


    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        return None

    def request_params(self, **kwargs) -> MutableMapping[str, Any]:
        return {}

    def request_headers(self, **kwargs) -> MutableMapping[str, Any]:
        return {"Authorization": self.api_key}

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        response_json = response.json()
        for resp in response_json:
            yield resp


class JobindsatsSubjects(JobindsatsApiStream):
    primary_key = "subjectid"

    def path(self, **kwargs) -> str:
        return "subjects"

class JobindsatsTables(JobindsatsApiStream):
    primary_key = "tableid"

    def path(self, **kwargs) -> str:
        return "tables"


# Source
class SourceJobindsatsApi(AbstractSource):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        try:
            headers = {"Authorization": config["api_key"]}

            resp = requests.get(f"{JobindsatsApiStream.url_base}subjects", headers=headers)
            status = resp.status_code
            logger.info(f"Ping response code: {status}")
            if status == 200:
                return True, None
            return False, resp.text
        except Exception as e:
            return False, e



    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        return [JobindsatsSubjects(config["api_key"]), JobindsatsTables(config["api_key"])]
