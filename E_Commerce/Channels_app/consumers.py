from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        self.send({
            'type': 'websocket.accept',    
        })

    def websocket_receive(self, event):
        self.send(
            {
                "type": 'websocket.send',
                "text": "hello i got your message from client side",
            }
        )
    
    def websocket_disconnect(self, event):
        self.send({
            'type': 'websocket.close',    
        })