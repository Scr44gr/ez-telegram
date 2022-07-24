# ez-telegram 🤖

A minimal client to get messages from telegram channels using webscraping. 

## Installation 📝
```bash
pip install git+https://github.com/Scr44gr/ez-telegram.git@main
```

## Usage 📖

```python
from ez_telegram import EzClient

client = EzClient()
messages = client.get_messages(channel="telegram")
print(message)
```

### You'll get a list of messages
```python
[
  'message',
  'message',
  'message',
  ...
]
```
