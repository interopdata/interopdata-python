# openapi_client.model.customer.Customer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. | 
**[description](#description)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**id** | str,  | str,  | A unique identifier of the customer in your system. | 
**[email](#email)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Customer’s email address. It’s displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to 512 characters. | 
**[preferredLocales](#preferredLocales)** | list, tuple,  | tuple,  | Customer’s preferred languages, ordered by preference. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# email

Customer’s email address. It’s displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to 512 characters.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Customer’s email address. It’s displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to 512 characters. | 

# description

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

# metadata

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. | 

# preferredLocales

Customer’s preferred languages, ordered by preference.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Customer’s preferred languages, ordered by preference. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

