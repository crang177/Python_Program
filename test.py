import requests,os
import time
import hashlib
from Crypto.Cipher import AES #解密AES
import base64 #由于抓包得到了密文被编码成了base64，所以要导入这个包进行改变编码方式
from Crypto.Util.Padding import unpad #清除生成AES解密以后的填充区域
import re


