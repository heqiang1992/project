#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Crypto.Hash.SHA256 import SHA256Hash
from hashlib import sha256
import random
import string
from Crypto.Random.random import StrongRandom

#
# verifier = ''.join(random.sample(string.ascii_letters + string.digits+"-"+"_", 43))
# print(verifier)
# challenge = SHA256Hash(verifier.encode("utf-8"))
# ccccc = challenge.digest()
# bbbbb = challenge.hexdigest()
# # challenge = sha256.update(verifier).digest()
# print(ccccc)
# print(bbbbb)
# print(len("PzMMWFik3rFfYfSgUWhBSgJOyuCQ3-b4Kwp5KtYnQcM"))

# sha256 = sha256()
# sha256.update(verifier.encode("utf-8"))
# print(sha256.digest())
# a = sha256.digest().decode("ansii")
# # b = str(a,'unicode')
# print(a)


import execjs

# def get_js():
#     f = open("D:\pkce.js", 'r', encoding='utf-8')
#     line = f.readline()
#     htmlstr = ''
#     while line:
#         htmlstr = htmlstr+line
#         line = f.readline()
#     return htmlstr
#
# def get_des_psswd():
#     jsstr = get_js()
#     ctx = execjs.compile(jsstr)
#     return (ctx.call('run'),32)
#
# get_des_psswd()

ctx = execjs.compile("""
       function run() {
	var crypto = require("crypto")
	
	function base64URLEncode(str) {
    return str.toString('base64')
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=/g, '');
}
	function sha256(buffer) {
    return crypto.createHash('sha256').update(buffer).digest();
}
	
	var verifier = base64URLEncode(crypto.randomBytes(32));
    var challenge = base64URLEncode(sha256(verifier));
    pair = [verifier,challenge]
	return pair
	}
""")  # 获取代码编译完成后的对象


verifier = ctx.call("run")
print(verifier)