# Whatsapp-Web

## About
- This is a tool to parse Whatsapp messenger on a web browser. This tool uses the Selenium module in Python 2.7 and 3.5 for parsing through Whatsapp messages. 

## Usage
This is primarily built as a parsing tool for students.

## Contributing
- The repository is open to contribution from all interested developers. Kindly send us Pull Requests with explanation as to what changes you have done.
- Also, you can write to us by opening an [Issue](https://github.com/salman-bhai/Whatsapp-Web/issues) and also solve a current issue if possible.
- A detailed explanantion of how we came to building this software is maintained at the [Wiki](https://github.com/salman-bhai/Whatsapp-Web/wiki) page.
- This repository was created and is currently maintained by @[salman-bhai](https://github.com/salman-bhai).

## License
- The software is registered under the [MIT License](https://github.com/salman-bhai/Whatsapp-Web/blob/master/LICENSE)

## Installation
- **Fork** this project to your GitHub account.
- After forking, enter the following commands in your terminal.

```
$ git clone https://github.com/salman-bhai/Whatsapp-Web
```
- After that get inside the repository and execute the following instructions
```
cd WhatsApp-Web
pip install virtualenv
virtualenv wa-web
source wa-web/bin/activate
pip install -r requirements.txt
```
- Make sure to install Google Chrome or Chromium browser on your OS or you can also use Mozilla Browser to run this application.

- Open the drivers directory and read the [README](drivers/README.md) file there and install the required drivers according to you convenience.

- If you're using Chrome Driver run the following instruction:
```
python main.py --chrome
```

- If you're using Gecko Driver run the following instruction:
```
python main.py --mozilla
```
