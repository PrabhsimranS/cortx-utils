# CORTX-Py-Utils: CORTX Python common library.
# Copyright (c) 2022 Seagate Technology LLC and/or its Affiliates
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# For any questions about this software or licensing,
# please email opensource@seagate.com or cortx-questions@seagate.com.

import asyncio
from http import HTTPStatus
import json
from typing import Any, Dict, Tuple
import os
import pathlib
import sys

if (sys.argv[1] == 'ceph'):
    #admin user credendials ceph
    ACCESS_KEY_ID = "W6Z1GT81G2RKJ9M3NUUT"
    SECRET_ACCESS_KEY = "RBoam7RGXXYBEWvCXCDqNT7lBFC0giw9LlAhh2Hk"
    #user credentials under test
    #ACCESS_KEY_ID = "G32ZSGDWEMWSGGXSQYFE"
    #SECRET_ACCESS_KEY = "SqMzrREDELIQMiICeA017npUlnEmBZGunuIe0eh1"
    HOST = "ssc-vm-g3-rhev4-2905.colo.seagate.com"
    PORT = 8000
    TEST_UID = 'testceph'
elif (sys.argv[1] == 'rgw'):
    #admin user credendials rgw
    ACCESS_KEY_ID = "sgiamadmin"
    SECRET_ACCESS_KEY = "ldapadmin"
    #user credentials under test
    #ACCESS_KEY_ID = "Z4G91HTP6E7GAPQ46XFE"
    #SECRET_ACCESS_KEY = "leLgn2A6T8YkcEdXAkpKtlYlN3CbYcvDDeBBwuSL"
    HOST = "ssc-vm-g2-rhev4-3185.colo.seagate.com"
    PORT = 30080
    TEST_UID = 'testrgw'
else :
    print("Invalid argument \nHelp : \"python3 set_quota_test.py ceph\" or \"python3 set_quota_test.py rgw\"")


#TEST_USER_NAME = 'rgwadmintest112'
#TEST_USER_DISPLAY_NAME = 'RGW admin test user'
#TEST_USER_EMAIL = 'rgwadmintestuser111@test.com'
#TEST_USER_ACCESS_KEY = 'QWERTY'
#TEST_USER_TENANT = 'newtnt112'

#TEST_UID = 'testceph'
#TEST_UID = 'testrgw'
TEST_QUOTA_TYPE_USER = 'user'
TEST_QUOTA_TYPE_BUCKET = 'bucket'
TEST_ENABLED = 'true' # possible vales true or false
TEST_MAX_SIZE = '1700'
TEST_MAX_SIZE_KB = '11'
TEST_MAX_OBJECTS = '-1'
TEST_FORMAT = 'json'
TEST_BUCKET = 'bucket111'

async def set_user_quota() -> Tuple[HTTPStatus, Dict[str, Any]]:
    """
    Illustrate S3Client signed_http_request work.

    Create IAM user by specifying parameters, HTTP method and path.
    :returns: HTTP status code and user information as parsed json.
    """

    rgwcli = S3Client(
        ACCESS_KEY_ID, SECRET_ACCESS_KEY, HOST, PORT, tls_enabled=False)
    user_params = {
        'uid': TEST_UID,
        'quota-type' : TEST_QUOTA_TYPE_USER,
        #'enabled' : TEST_ENABLED,
        'max-size' : TEST_MAX_SIZE,
        #'max-size-kb' : TEST_MAX_SIZE_KB,
        #'max-objects' : TEST_MAX_OBJECTS,
        #'format' : TEST_FORMAT
    }
    print(f'Request Paramaters:\n {user_params}')
    #status, body = await rgwcli.signed_http_request(
    #    'PUT', '/admin/user?quota', query_params=user_params)
    status = await rgwcli.signed_http_request(
        'PUT', '/admin/user?quota', query_params=user_params)
    #user_info = json.loads(body)
    #return status, user_info
    return status

async def set_bucket_quota() -> Tuple[HTTPStatus, Dict[str, Any]]:
    """
    Illustrate S3Client signed_http_request work.

    Create IAM user by specifying parameters, HTTP method and path.
    :returns: HTTP status code and user information as parsed json.
    """

    rgwcli = S3Client(
        ACCESS_KEY_ID, SECRET_ACCESS_KEY, HOST, PORT, tls_enabled=False)
    user_params = {
        'uid': TEST_UID,
        'quota-type' : TEST_QUOTA_TYPE_BUCKET,
        'enabled' : TEST_ENABLED,
        'max-size' : TEST_MAX_SIZE,
        #'max-size-kb' : TEST_MAX_SIZE_KB,
        #'max-objects' : TEST_MAX_OBJECTS,
        'bucket' : TEST_BUCKET
        #'format' : TEST_FORMAT
    }
    print(f'Request Paramaters:\n {user_params}')
    #status, body = await rgwcli.signed_http_request(
    #    'PUT', '/admin/user?quota', query_params=user_params)
    status = await rgwcli.signed_http_request(
        'PUT', '/admin/user?quota', query_params=user_params)
    #user_info = json.loads(body)
    #return status, user_info
    return status

async def set_individual_bucket_quota() -> Tuple[HTTPStatus, Dict[str, Any]]:
    """
    Illustrate S3Client signed_http_request work.

    Create IAM user by specifying parameters, HTTP method and path.
    :returns: HTTP status code and user information as parsed json.
    """

    rgwcli = S3Client(
        ACCESS_KEY_ID, SECRET_ACCESS_KEY, HOST, PORT, tls_enabled=False)
    user_params = {
        'uid': TEST_UID,
        'quota-type' : TEST_QUOTA_TYPE_BUCKET,
        'enabled' : TEST_ENABLED,
        'max-size' : TEST_MAX_SIZE,
        #'max-size-kb' : TEST_MAX_SIZE_KB,
        #'max-objects' : TEST_MAX_OBJECTS,
        'bucket' : TEST_BUCKET
        #'format' : TEST_FORMAT
    }
    print(f'Request Paramaters:\n {user_params}')
    #status, body = await rgwcli.signed_http_request(
    #    'PUT', '/admin/user?quota', query_params=user_params)
    status = await rgwcli.signed_http_request(
        'PUT', '/admin/bucket?quota', query_params=user_params)
    #user_info = json.loads(body)
    #return status, user_info
    return status



if __name__ == "__main__":
    # The following three lines are required to run the sample from the sources
    # i.e. freshly cloned cortx-utils repo.
    # Prerequisite: in py-utils folder create the soft link to src named cortx
    # ln -s src cortx
    py_utils_rel_path = os.path.join(os.path.dirname(pathlib.Path(__file__)), '../../../..')
    sys.path.insert(1, py_utils_rel_path)
    from cortx.utils.s3 import S3Client

    loop = asyncio.get_event_loop()
    #status, user_info = loop.run_until_complete(set_quota())
    #print(f'{status} :: {user_info}')
    #status = loop.run_until_complete(set_user_quota())
    #status = loop.run_until_complete(set_bucket_quota())
    status = loop.run_until_complete(set_individual_bucket_quota())
    print(f'Response : \n {status}')
