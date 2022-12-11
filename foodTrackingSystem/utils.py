from web3 import Web3


def sendTransaction(message):
    # w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/7b0a01a78c194db5a22d2c293fd1eb27'))
    w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/7b0a01a78c194db5a22d2c293fd1eb27'))
    address = '0x6dd071cd9D86ac606172F54A2f84eE8EC85fF74B'
    privateKey = '0x5b335d0a5534183b3a84aaa9fdc347a15b0aebf0642201ab694019c19e59d690'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',  # 42 char
        value=value,
        data=message.encode('utf-8')
    ), privateKey)

    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId
