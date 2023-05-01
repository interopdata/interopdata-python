import typing_extensions

from interopdata.apis.tags import TagValues
from interopdata.apis.tags.interopdata_api import InteropdataApi
from interopdata.apis.tags.default_api import DefaultApi

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
