#!/bin/bash

<GetCategoriesRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <RequesterCredentials>
    <eBayAuthToken>****TOKEN HERE***</eBayAuthToken>
  </RequesterCredentials>
    <CategorySiteID>0</CategorySiteID>
    <DetailLevel>ReturnAll</DetailLevel>
</GetCategoriesRequest> ' | xmllint --format -
