from sqlite3 import connect
from pydantic import BaseModel
from fastapi import FastAPI
import pika
from rmq import MessageServer

app = FastAPI()

recieved_message_list = []
sent_message_list = []
incoming_message_list = []
class Message(BaseModel):
    message: str

#set params for queue
#send message
#num messages
#queue name

@app.get("/")
async def startup():
    return 'The API is currently running'

@app.get("/send1/")
async def send():
    connect = MessageServer()
    connect.send_messages("test")
    sent_message_list.append(len(sent_message_list))
    return {
        'message_count' : len(sent_message_list),
        'data' : sent_message_list
    }

@app.get("/send/")
async def send():
    connect = MessageServer()
    connect.send_message("test")
    sent_message_list.append(len(sent_message_list))
    return {
        'message_count' : len(sent_message_list),
        'data' : sent_message_list
    }

@app.get("/messages/")
async def messages():
    connect = MessageServer()
    return connect.receieve_messages(num_messages=1)

#feedback
#better comments
#better whitespace
#better naming
#global variables
#increase testing


#room - name participants
#DEQUEUE
    #takes:
#       roomName,
#       roomType, 100public 200private
#       memberlist, -addtogroup -removefromgroup methods
#       ownerAlias,
#       createNew
#
#       props
#       dirty flag for persistence
#       createTime, ModifyTime
#       persist and restore methods that go to MONGO
#
#       methods
#       get_messages(num_messages: int, return_objects: bool) -> list of ChatMessage
#       send_message(message: str, mess_props: MessageProperties) -> bool
#       find_message(message_text: str) -> ChatMessage
#       get() -> ChatMessage – gets the next message in the deque from the right
#       put(message: ChatMessage) -> None – puts message into the (left of the) queue
#
#
#   MessageProperties() that holds the following properties:
#       mess_type: int - message type – either sent or received.
# o You should have constants for the type
#       room_name: str - room to which the message belongs
#       to_user: str – destination for message. Can be group exchange
#       from_user: str – alias that is the sender of the message
#       sent_time: datetime – timestamp for when the message was sent
#       rec_time: datetime – timestamp for when the message was received
#       sequence_number: int – number of the message in the sequence of messages
#
# You should have a class called ChatMessage():
#       property message: str - the actual chat message
#       property mess_id: id returned by MongoDB after saving
#       property mess_props: MessageProperties – the message properties
#       property dirty: bool – flag for if an instance needs to be saved

# I find it useful to have a RoomList class. You can either inherit list or create an internal private list that holds the list of rooms. Properties and Methods you should have:
# ·     Name: the list name.
# ·     Constructor: just takes name: str for the name of the list
# ·     Either inherit from list or create an internal __rooms: list property
# ·     add: add a new RoomChat instance to the list
#       remove: remove a RoomChat instance from the list
# ·     find: find a RoomChat instance by name
# ·     find_by_member: return all chatrooms that have the alias as a member
# ·     find_by_owner: return all chatrooms that have the alias as the owner
# ·     persist and restore, saving the list metadata and restoring the list metadata
#       After saving or restoring the metadata, iterate through all rooms in the list calling their persist or restore methods
#







