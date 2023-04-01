from datetime import datetime
from encription import genrateHash as GH


class block:

    def __init__(self, MarkelRoot, previous_hash, nonce):

        """
            This is the init function for the block class.
            This will be resposible for setting up the block class.

            Parameters:
            MarkelRoot (str): The Markel Root of the block.
            previous_hash (str): The previous hash of the block.
            nonce (int): The nonce of the block.

            Returns:
            None.
        """
        self.timestamp = datetime.now()
        self.MarkelRoot = MarkelRoot
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.GH(f"{self.MarkelRoot}{self.timestamp}{self.nonce}{self.previous_hash}")
    
    def __str__(self):
        return f"Block Hash: {self.hash}\nMarkel Root: {self.MarkelRoot}\nTimestamp: {self.timestamp}\nNonce: {self.nonce}\nPrevious Hash: {self.previous_hash}"
    