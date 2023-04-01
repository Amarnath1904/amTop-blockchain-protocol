import socket
import os



class ANSHI:

    """
        ANSHI alpha networking sharing interface

        This is a networking sharing interface that allows you to share files between two devices on the amTop network.
        This will be resposible for the networking side of the amTop network.

    
    """


    def __init__(self):

        """
            This is the init function for the ANSHI class.
            This will be resposible for setting up the socket and getting the basic info for the ANSHI class.
        """
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.IP = None
        self.PORT = 6969
        self.ADDR = (self.IP, self.PORT)
        self.FORMAT = 'utf-8'
        self.getBasicInfo()
    
    def server(self, Function, file = None, FilenameTosave = None):

        """
            Sends or receives files over a socket connection as a server.

            Parameters:
            Function (str): Either 'send' or 'receive', indicating the desired file transfer operation.
            file (str): The name of the file to be sent, or None if receiving a file.
            FilenameTosave (str): The name to save the received file as, or None if sending a file.

            Raises:
            Exception: If no file is provided when sending, or if no file name is provided when receiving.

            Returns:
            None.

        """


        self.s.bind(self.ADDR)
        self.s.listen()
        if Function == 'send':
            if file == None:
                raise Exception('No file to send')
            if file != None:
                while True:
                    conn, addr = self.s.accept()
                    with open(file, 'rb') as f:
                        data = f.read()
                        Filesize = "next file size: " + str(os.path.getsize(file))
                        conn.send(Filesize.encode(self.FORMAT))
                        conn.send(data)
                        conn.close()
        elif Function == 'recive':
            if FilenameTosave == None:
                raise Exception('provide file name to save')
            else:
                while True:
                    conn, addr = self.s.accept()
                    filesize = conn.recv(1024).decode(self.FORMAT)
                    filesize = int(filesize.replace('next file size: ', ''))
                    data = conn.recv(filesize)
                    with open(FilenameTosave, 'wb') as f:
                        f.write(data)
                        conn.close()


    def client(self, Function, connectInfo, file = None, FilenameTosave = None):

        """
            Sends or receives files over a socket connection as a client.

            Parameters:
            Function (str): Either 'send' or 'receive', indicating the desired file transfer operation.
            file (str): The name of the file to be sent, or None if receiving a file.
            FilenameTosave (str): The name to save the received file as, or None if sending a file.
            connectInfo (tuple): A tuple containing the server IP address and port number to connect to.

            Raises:
            Exception: If no file is provided when sending, or if no file name is provided when receiving.
            Exception: If no connection info is provided, or if the provided info is not a tuple.

            Returns:
            None.

        """


        if connectInfo == None:
            raise Exception('No connect info provided')
        elif connectInfo is not tuple:
            raise Exception('connect info must be a tuple')
        self.s.connect(connectInfo)
        if Function == 'send':
            if file == None:
                raise Exception('No file to send')
            if file != None:
                with open(file, 'rb') as f:
                    data = f.read()
                    Filesize = "next file size: " + str(os.path.getsize(file))
                    self.s.send(Filesize.encode(self.FORMAT))
                    self.s.send(data)
                    self.s.close()
        elif Function == 'recive':
            if FilenameTosave == None:
                raise Exception('provide file name to save')
            else:
                filesize = self.s.recv(1024).decode(self.FORMAT)
                filesize = int(filesize.replace('next file size: ', ''))
                data = self.s.recv(filesize)
                with open(FilenameTosave, 'wb') as f:
                    f.write(data)
                    self.s.close()


    def fileHandel(self, reseverType, Function, ConnectInfo,file = None, FileTosave = None):

        """
            Sends or receives files between a client and a server using sockets.

        Args:
            file (str, optional): Path to the file to be sent. Defaults to None.
            receiver_type (str): Specifies whether the current process is acting as a 'Server' or 'Client'.
            connect_info (tuple): A tuple containing the IP address and port number to connect to.
            function (str): The operation to perform. Either 'send' or 'receive'.
            file_to_save (str, optional): Path to the file to be saved on the receiving end. Defaults to None.

        Returns:
            None

        Raises:
            Exception: If a required argument is missing or invalid.
        """
        if function == 'send':
            if reseverType == 'Server':
                self.client(Function, file, connectInfo = ConnectInfo)
            elif reseverType == 'Client':
                self.server(Function, file)
        elif function == 'recive':
            if reseverType == 'Server':
                self.client(Function, connectInfo = ConnectInfo, FilenameTosave = FileTosave)
            elif reseverType == 'Client':
                self.server(Function, FilenameTosave = FileTosave)
        elif function is not str:
            raise Exception("Plese provide a valid function ('send' or 'recive')")
        
    def getBasicInfo(self):
        if self.IP == None:
            amTopServerInfo = ("122.162.98.69", 6969)
            self.s.connect(amTopServerInfo)
            self.s.send("get info".encode(self.FORMAT))
            self.IP = self.s.recv(1024).decode(self.FORMAT)
