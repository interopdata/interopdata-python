import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.interopdata_api import InteropdataApi
from openapi_client.apis.tags.default_api import DefaultApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.INTEROPDATA: InteropdataApi,
        TagValues.DEFAULT: DefaultApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.INTEROPDATA: InteropdataApi,
        TagValues.DEFAULT: DefaultApi,
    }
)
