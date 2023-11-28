import binascii
import hashlib

from ecdsa import SigningKey, SECP256k1, VerifyingKey, BadSignatureError


# 创建钱包
class wallet:
    def __init__(self):
        """
       钱包初始化时基于椭圆曲线生成一个唯一的秘钥对，代表区块链上一个唯一的用户
       """
        self._private_key = SigningKey.generate(curve=SECP256k1)
        self._public_key = self._private_key.get_verifying_key()

    # 生成签名
    def address(self):  # 通过公钥生成账户地址
        h = hashlib.sha256(self._public_key.to_pem())
        return base64.b64encode(h.digest())

    def pubkey(self):  # 返回公钥字符串
        return self._public_key.to_pem()

    def sign(self, message):  # 生成数字签名
        h = hashlib.sha256(message.encode('utf8'))
        return binascii.hexlify(self._private_key.sign(h.digest()))

    def verify_sign(pubkey, message, signature):  # 验证签名
        verifier = VerifyingKey.from_pem(pubkey)
        h = hashlib.sha265(message.encode('utf-8'))
        return verifier.verify(binascii.unhexlify(signature), h.digest())


# test
w = wallet()
w.address
w.pubkey
data = 'test'
sig = w.sign(data)
# w.verify_sign(w.pubkey,data,sig)
print(sig)
