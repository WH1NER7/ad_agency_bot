import motor.motor_asyncio


class MongoDBConnection:
    def __init__(self, host='localhost', port=27017, db_name=None):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.client = None
        self.db = None

    async def connect(self):
        try:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(self.host, self.port)
            self.db = self.client[self.db_name]
            print(f'Connected to MongoDB. Host: {self.host}, Port: {self.port}, Database: {self.db_name}')
        except Exception as e:
            print(f'Error connecting to MongoDB: {str(e)}')

    async def disconnect(self):
        if self.client:
            self.client.close()
            print('Disconnected from MongoDB')

    def get_collection(self, collection_name):
        print(collection_name)
        return self.db[collection_name]

    async def insert_data(self, collection_name, data):
        collection = self.get_collection(collection_name)
        result = await collection.insert_one(data)
        print(f'Data inserted. Inserted ID: {result.inserted_id}')
