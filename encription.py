import mnemonic
from hashlib import sha256
import rsa


class nodeinfo:
    """
        This class is used to store the information of the node.

    """
    def __init__(self):
        self.publickey = None
        self.privatekey = None
        self.mnemonic = None
        self.ntworkOn = "amTop"
        self.nodeID = None

def generatekeys():
    """
        This function is used to generate the public and private keys for the node.
    """
    (pubkey, privkey) = rsa.newkeys(1024)

    with open('public.pem', 'w+') as f:
        f.write(pubkey.save_pkcs1().decode('utf8'))
    with open('private.pem', 'w+') as f:
        f.write(privkey.save_pkcs1().decode('utf8'))


    return pubkey, privkey
def generateMnemonic():
    """
        This function is used to generate the mnemonic for the node.
    """

    with open('mnemonic.txt', 'w+') as f:
        f.write(mnemonic.Mnemonic('english').generate(strength=256))

    return mnemonic.Mnemonic('english').generate(strength=256)

def genrateHash(data):
    """
        This function is used to generate the hash for the node.
    """
    return sha256(data.encode()).hexdigest()
def genrateprivatekey(mnemonic):
    """
        This function is used to generate the private key for the node.
    """
    return mnemonic.to_seed(mnemonic)