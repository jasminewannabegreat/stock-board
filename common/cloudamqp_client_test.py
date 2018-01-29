from cloudamqp_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://yuyxpmht:1rPzdMcZhSzwlr9OdLLNN4Ey4q0tfbWX@donkey.rmq.cloudamqp.com/yuyxpmht"
TEST_QUEUE_NAME = "stocks-queue"

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)
    
    sentMsg = {"test":"test"}
    client.sendMessage(sentMsg)
    receivedMsg = client.getMessage()

    assert sentMsg == receivedMsg
    print "test_basic passed."

if __name__ == "__main__":
    test_basic()