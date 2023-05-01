# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    DATASETS = "/datasets"
    DATAEXPORTS = "/data-exports"
    DATAEXPORTS_ID = "/data-exports/{id}"
    OAUTH_TOKEN = "/oauth/token"
    CUSTOMERS = "/customers"
    DATAEXPORTLINKS = "/data-export-links"
    DATAEXPORTDATASETS_ID = "/data-export-datasets/{id}"
    DATAEXPORTDATASETS_ID_DOWNLOAD = "/data-export-datasets/{id}/download"
