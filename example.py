from ez_telegram import EzClient


if __name__ == '__main__':
    client = EzClient()
    print(client.get_messages(channel='telegram')[-1]) # Prints the last message from the telegram channel.