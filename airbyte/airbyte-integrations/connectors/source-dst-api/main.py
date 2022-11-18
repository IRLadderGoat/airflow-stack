#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_dst_api import SourceDstApi

if __name__ == "__main__":
    source = SourceDstApi()
    launch(source, sys.argv[1:])
