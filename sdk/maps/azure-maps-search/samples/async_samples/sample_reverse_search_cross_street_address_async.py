# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_reverse_search_cross_street_address_async.py
DESCRIPTION:
    This sample demonstrates how to perform reverse search cross street address.
USAGE:
    python sample_reverse_search_cross_street_address_async.py

    Set the environment variables with your own values before running the sample:
    - AZURE_SUBSCRIPTION_KEY - your subscription key
"""
import asyncio
import os

subscription_key = os.getenv("AZURE_SUBSCRIPTION_KEY")


async def reverse_search_cross_street_address_async():
    # [START reverse_search_cross_street_address_async]
    from azure.core.credentials import AzureKeyCredential
    from azure.maps.search.aio import MapsSearchClient

    maps_search_client = MapsSearchClient(credential=AzureKeyCredential(subscription_key))

    async with maps_search_client:
        result = await maps_search_client.reverse_search_cross_street_address(coordinates=(25.0338053, 121.5640089))

    print("Get Search Address Reverse Cross Street:")
    print(result)
    # [END reverse_search_cross_street_address_async]

if __name__ == '__main__':
    asyncio.run(reverse_search_cross_street_address_async())