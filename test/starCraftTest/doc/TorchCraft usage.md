#TorchCraft usage
##definition
	Server = the part of the code that runs along with StarCraft (that is where we instantiate a ZMQ server).
	Client = the part of the code that runs in Torch, consumes data (state) from the server and sends commands (actions).

##PC server (runs StarCraft:Brood War)
1.Open $StarCraft/BWAPI/Chaoslauncher.
2.Run Chaoslauncher-MultiInstance.exe as Administrator.
3.Choose BWAPI 4.1.2 Injector [RELEASE].
4.Click Start button.

##Ubuntu client
1.Start a terminal.
2.cd ~/torch/TorchCraft/examples/py.
3.python *.py -t 192.168.10.113(server's ip address).
4.enjoy the game :)


