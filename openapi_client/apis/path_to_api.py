import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.datasets import Datasets
from openapi_client.apis.paths.data_exports import DataExports
from openapi_client.apis.paths.data_exports_id import DataExportsId
from openapi_client.apis.paths.oauth_token import OauthToken
from openapi_client.apis.paths.customers import Customers
from openapi_client.apis.paths.data_export_links import DataExportLinks
from openapi_client.apis.paths.data_export_datasets_id import DataExportDatasetsId
from openapi_client.apis.paths.data_export_datasets_id_download import DataExportDatasetsIdDownload

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.DATASETS: Datasets,
        PathValues.DATAEXPORTS: DataExports,
        PathValues.DATAEXPORTS_ID: DataExportsId,
        PathValues.OAUTH_TOKEN: OauthToken,
        PathValues.CUSTOMERS: Customers,
        PathValues.DATAEXPORTLINKS: DataExportLinks,
        PathValues.DATAEXPORTDATASETS_ID: DataExportDatasetsId,
        PathValues.DATAEXPORTDATASETS_ID_DOWNLOAD: DataExportDatasetsIdDownload,
    }
)

path_to_api = PathToApi(
    {
        PathValues.DATASETS: Datasets,
        PathValues.DATAEXPORTS: DataExports,
        PathValues.DATAEXPORTS_ID: DataExportsId,
        PathValues.OAUTH_TOKEN: OauthToken,
        PathValues.CUSTOMERS: Customers,
        PathValues.DATAEXPORTLINKS: DataExportLinks,
        PathValues.DATAEXPORTDATASETS_ID: DataExportDatasetsId,
        PathValues.DATAEXPORTDATASETS_ID_DOWNLOAD: DataExportDatasetsIdDownload,
    }
)
