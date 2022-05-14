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
    ACCESS_KEY_ID = "QBNHFX24T0HLBA0NW7GV"
    SECRET_ACCESS_KEY = "5oBdWYcKZ7zzpl9IVdGPs4F56BziUHlI61ScHGS1"
    HOST = "ssc-vm-g3-rhev4-2905.colo.seagate.com"
    PORT = 8000
    TEST_USER_NAME = 'testuser1'
elif (sys.argv[1] == 'rgw'):
    #admin user credendials rgw
    ACCESS_KEY_ID = "sgiamadmin"
    SECRET_ACCESS_KEY = "ldapadmin"
    HOST = "ssc-vm-g2-rhev4-3185.colo.seagate.com"
    PORT = 30080
    TEST_USER_NAME = 'testrgw'
else :
    print("Invalid argument \nHelp : \"python3 get_user_info.py ceph\" or \"python3 get_user_info.py rgw\"")

#TEST_USER_NAME = 'testceph'
#TEST_USER_NAME = 'testrgw'
#TEST_USER_DISPLAY_NAME = 'RGW admin test user'
#TEST_USER_EMAIL = 'rgwadmintestuser1@test.com'
TEST_BUCKET_NAME = 'bucket11'

async def get_user_capacity() -> Tuple[HTTPStatus, Dict[str, Any]]:

    """

    Illustrate S3Client signed_http_request work.


    Create IAM user by specifying parameters, HTTP method and path.

    :returns: HTTP status code and user information as parsed json.

    """


    rgwcli = S3Client(

        ACCESS_KEY_ID, SECRET_ACCESS_KEY, HOST, PORT, tls_enabled=False)

    user_params = {

        #'display-name': TEST_USER_DISPLAY_NAME,

        #'email': TEST_USER_EMAIL,

        'uid': TEST_USER_NAME,
        #'format': 'xml',
        #'bucket' : TEST_BUCKET_NAME

    }

    status, body = await rgwcli.signed_http_request(

        'GET', '/admin/usage', query_params=user_params)
    #user_info = json.loads(body)

    #return status, user_info
    return status, body

if __name__ == "__main__":
    # The following three lines are required to run the sample from the sources
    # i.e. freshly cloned cortx-utils repo.
    # Prerequisite: in py-utils folder create the soft link to src named cortx
    # ln -s src cortx
    py_utils_rel_path = os.path.join(os.path.dirname(pathlib.Path(__file__)), '../../../..')
    sys.path.insert(1, py_utils_rel_path)
    from cortx.utils.s3 import S3Client

    loop = asyncio.get_event_loop()
    status, user_info = loop.run_until_complete(get_user_capacity())
    print(f'{status} :: {user_info}')
