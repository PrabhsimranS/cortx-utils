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

ACCESS_KEY_ID = "sgiamadmin"
SECRET_ACCESS_KEY = "ldapadmin"
HOST = "ssc-vm-g2-rhev4-3185.colo.seagate.com"
PORT = 30080

TEST_USER_NAME = sys.argv[1]
print(f'TEST_USER_NAME- {TEST_USER_NAME}')


async def delete_user() -> Tuple[HTTPStatus, Dict[str, Any]]:

    """

    Illustrate S3Client signed_http_request work.


    Create IAM user by specifying parameters, HTTP method and path.

    :returns: HTTP status code and user information as parsed json.

    """


    rgwcli = S3Client(

        ACCESS_KEY_ID, SECRET_ACCESS_KEY, HOST, PORT, tls_enabled=False)

    user_params = {

        'uid': TEST_USER_NAME,

    }

    status = await rgwcli.signed_http_request(

        'DELETE', '/admin/user', query_params=user_params)

    #user_info = json.loads(body)

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
    status = loop.run_until_complete(delete_user())
    print(f'{status}')

    """
    for i in range(2,1001):
        loop = asyncio.get_event_loop()
        TEST_USER_NAME = 'newtnt1$cortxnewuser'+str(i)
        print(f'TEST_USER_NAME:{TEST_USER_NAME}')
        status = loop.run_until_complete(delete_user())
        print(f'{status} :: {user_info}')
    """
