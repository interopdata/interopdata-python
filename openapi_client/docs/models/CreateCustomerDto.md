# openapi_client.model.create_customer_dto.CreateCustomerDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | A unique identifier of the customer in your system. | 
**email** | str,  | str,  | Customer’s email address. It’s displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to 512 characters. | [optional] 
**name** | str,  | str,  | The customer’s full name or business name. | [optional] 
**description** | str,  | str,  | An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard. | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. | [optional] 
**[preferredLocales](#preferredLocales)** | list, tuple,  | tuple,  | Customer’s preferred languages, ordered by preference. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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

