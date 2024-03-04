from twisted.internet import reactor, protocol
import pyaudio
import threading

class AudioServer(protocol.Protocol):
    def dataReceived(self, data):
        stream.write(data)

class AudioServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return AudioServer()

def receive_audio():
    reactor.listenTCP(12345, AudioServerFactory())
    reactor.run(installSignalHandlers=0)

def send_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)

    while True:
        data = stream.read(1024)
        if hasattr(send_audio, 'client_protocol'):
            send_audio.client_protocol.transport.write(data)

# Start two threads - one for receiving, one for sending
receive_thread = threading.Thread(target=receive_audio)
send_thread = threading.Thread(target=send_audio)

# Set the client protocol in the send_audio function
def set_client_protocol(protocol):
    send_audio.client_protocol = protocol

# Pass the set_client_protocol function to the receive thread
receive_thread.client_callback = set_client_protocol

receive_thread.start()
send_thread.start()

# Wait for the threads to finish (you can add a condition to exit the program)
receive_thread.join()
send_thread.join()
