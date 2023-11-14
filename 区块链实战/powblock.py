import hashlib
from datetime import datetime 

class Block:
   def __init__(self,data,prev_hash):
           self.prev_hash=prev_hash
           self.data=data
           self.timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           #pow
           self.nonce=None
           self.hash=None
   def __repr__(self):
           return "data:%s,hash:%s" % (self.data,self.hash)
           
           
class ProofOfWork:
  def __init__(self,block,difficult=5):
           self.block=block
           self.difficulty=difficult#表示有效的哈希值以5个"0"开头
  def mine(self):#挖矿函数
           i=0
           prefix='0'*self.difficulty
           while True:
             message=hashlib.sha256()
             message.update(str(self.block.prev_hash).encode('utf-8'))
             message.update(str(self.block.data).encode('utf-8'))
             message.update(str(self.block.timestamp).encode('utf-8'))
             message.update(str(i).encode('utf-8'))
             digest=message.hexdigest()
             if digest.startswith(prefix):
               self.block.nonce=i
               self.block.hash=digest
               return self.block
             i+=1
  def validate(self):#验证有效性
           message=hashlib.sha256()
           message.update(str(self.block.prev_hash).encode('utf-8'))
           message.update(str(self.block.data).encode('utf-8'))
           message.update(str(self.block.timestamp).encode('utf-8'))
           message.update(str(self.block.nonce).encode('utf-8'))
           digest=message.hexdigest()
           
           prefix='0'*self.difficulty
           return digest.startswith(prefix)
  
           '''
           #test
b=Block(data="测试",prev_hash="")
w=ProofOfWork(b)
valid_block=w.mine()
w.validate()
print(b.data,b.prev_hash,b.timestamp,w.block.hash,w.block.nonce)
   '''               

           
class BlockChain:
          
          def __init__(self):
           self.blocks = []#IndentationError: expected an indented block——>解决方案：错误逻辑代码前空格，相当于Java、c里的{}
          def add_block(self,block):
           self.blocks.append(block)
        
'''
#实现区块链原型
'''
#创世区块
#再创建两个区块
#有效性【挖矿】
genesis_block=Block(data="创世区块",prev_hash="")
n0=ProofOfWork(genesis_block)
v0=n0.mine()
n0.validate()

new_block=Block(data="cwy sent 1314 bitcoin to mkx",prev_hash=genesis_block.hash)
n1=ProofOfWork(new_block)
v1=n1.mine()
n1.validate()

new_block2=Block(data="cwy sent 520 bitcoin to mkx",prev_hash=new_block.hash)
n2=ProofOfWork(new_block2)
v2=n2.mine()
n2.validate()

new_block3=Block(data="cwy sent 1314 bitcoin to mkx",prev_hash=new_block2.hash)
n3=ProofOfWork(new_block3)
v3=n3.mine()
n3.validate()

new_block4=Block(data="cwy sent 520 bitcoin to mkx",prev_hash=new_block3.hash)
n4=ProofOfWork(new_block4)
v4=n4.mine()
n4.validate()



#print(genesis_block.hash)
#新建一个区块链

blockchain = BlockChain()

blockchain.add_block(genesis_block)
blockchain.add_block(new_block)
blockchain.add_block(new_block2)
blockchain.add_block(new_block3)
blockchain.add_block(new_block4)

#打印区块链
i=1
for block in blockchain.blocks: 
    print('------------------------------',"第%d个区块信息:" % i,'------------------------------')
    print("prev_hash: %s" % block.prev_hash)
    print("contect: %s" % block.data)
    print("hash: %s" % block.hash)
    print("nonce: %d" % block.nonce)
    print("timestamp: %s" % block.timestamp)
    print("\n")
    i+=1
print("区块链包含区块个数:%d\n" % len(blockchain.blocks))










































