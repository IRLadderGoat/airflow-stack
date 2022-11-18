#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_jobindsats_api import SourceJobindsatsApi

if __name__ == "__main__":
    source = SourceJobindsatsApi()
    launch(source, sys.argv[1:])
