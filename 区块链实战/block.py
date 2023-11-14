'''
区块包括区块头和区块体
#区块头：版本、父区块哈希值、数据、merkle根、时间戳、目标难度、nonce值
#区块体：实际上可以包含任何内容-在比特币中包括交易输入数量、交易输出数量和长度不定的交易记录等信息

注：这里开发的区块链系统简化了区块的结构【父区块哈希值、数据、时间戳、哈希值】

区块的哈希值=hash(父区块哈希值.数据.时间戳)
'''

import hashlib
from datetime import datetime 

class Block:

   def __init__(self,data,prev_hash):
           #
           self.prev_hash=prev_hash
           self.data=data
           #
           self.timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
           #
           message=hashlib.sha256()
           message.update(str(self.prev_hash).encode('utf-8'))
           message.update(str(self.data).encode('utf-8'))
           message.update(str(self.timestamp).encode('utf-8'))
           self.hash=message.hexdigest()
           
'''
定义区块链结构：将区块通过哈希值前后依次相连，然后将这些区块放到一个列表中，再定义一个函数来实现向这个列表添加区块的功能
'''
class BlockChain:
          
          def __init__(self):
           self.blocks = []#IndentationError: expected an indented block——>解决方案：错误逻辑代码前空格，相当于Java、c里的{}
          def add_block(self,block):
           self.blocks.append(block)
        
'''
实现区块链原型
'''
#创世区块
genesis_block=Block(data="创世区块",prev_hash="")
#再创建两个区块
new_block=Block(data="cwy sent 1314 bitcoin to mkx",prev_hash=genesis_block.hash)
new_block2=Block(data="cwy sent 520 bitcoin to mkx",prev_hash=new_block.hash)
#print(genesis_block.hash)
#新建一个区块链

blockchain = BlockChain()

blockchain.add_block(genesis_block)
blockchain.add_block(new_block)
blockchain.add_block(new_block2)


#打印区块链
print("区块链包含区块个数:%d\n" % len(blockchain.blocks))


for block in blockchain.blocks: 
    print("父区块区块哈希: %s" % block.prev_hash)
    print("区块内容: %s" % block.data)
    print("区块哈希: %s" % block.hash)
    print("\n")













































