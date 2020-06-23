# Chat-Room-101
<p align="center">
    <img src="https://i.ibb.co/JHjgVtZ/Logo.png" alt="Logo" border="0">
    <br>A Simple GUI based Chat Room Application.
</p>

---

[![GitHub pull-requests](https://img.shields.io/github/issues-pr/SVijayB/Chat-Room-101.svg)](https://github.com/SVijayB/Chat-Room-101/pulls)
[![GitHub issues](https://img.shields.io/github/issues/SVijayB/Chat-Room-101.svg)](https://github.com/SVijayB/Chat-Room-101/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/SVijayB/Chat-Room-101.svg)](https://github.com/SVijayB/Chat-Room-101/graphs/contributors)

[![GitHub license](https://img.shields.io/github/license/SVijayB/Chat-Room-101.svg)](https://github.com/SVijayB/Chat-Room-101/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/release/SVijayB/Chat-Room-101.svg)](https://github.com/SVijayB/Chat-Room-101/releases)
[![GitHub repo size](https://img.shields.io/github/repo-size/SVijayB/Chat-Room-101)](https://github.com/SVijayB/Chat-Room-101)

[![Code of Conduct](https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=flat)](https://github.com/SVijayB/Chat-Room-101/blob/master/.github/CODE_OF_CONDUCT.md)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/SVijayB/Chat-Room-101/blob/master/.github/CONTRIBUTING.md)

## Table of Contents

- [Motivation](#Motivation)
- [Usage](#Usage)
- [Contributing](#Contributing)
- [License](#License)

## Motivation

<p align="center">
    <a href="https://github.com/SVijayB/Chat-Room-101"><img src="https://i.ibb.co/3TxfKt3/SS.png" alt="Logo" border="0"></a>
</p>

This application was built to create a simple and easy to use interface for sending and receiving messages.

This application works on TCP connections made between devices over the internet.
Hence, messages are sent and recieved securely.

## Usage

For the latest Stable version, go to <a href="https://github.com/SVijayB/Chat-Room-101/releases">Releases</a>

As an alternative, you could also clone the repository using `git clone https://github.com/SVijayB/Chat-Room-101.git`

### Server Side :
#### Internal Server : 
If you want to host your own Chat room where all devices are conencted to the same router, 
run the `Server.py` script present in the `src` directory.
Send your clients the IP address and the port you are using (default = 8080)

#### External Server : 
If you want people connected to a different router to connect to the server, port-forwarding is the only option.<br>
Its really not that hard. Just follow the below steps.
- Use `ifconfig` on linux or mac and `ipconfig` on windows comand line.
- Copy the Default Gateway IP Address value and your IPv4 Address.
- Paste the Default Gateway Address on any browser url and login with your router credentials.
- Go to advanced settings and search for options like NAT forwarding or virtual servers.
- Set up a virtual server, select service type as `SOCK` or `Socket`. 
- Choose port `8080` for both internal and external connection.
- Paste your IPv4 Address value as your internal IP.
- Set protocol as `TCP` or All

Once done, run it. You are good to go.

**NOTE:** You will have to share your external IP for the clients to connect to your server. 
To do this, go <a href="https://whatismyipaddress.com/">here</a> and send your clients your `IPv4 Address`.

### Client Side : 
For Client side, run the `Client.py` script present in the `src` directory.
Enter the Host IP address and the Port number.

## Contributing 

To contribute to Steam_WebScrapper, fork the repository, create a new branch and send us a pull request. Make sure you read [CONTRIBUTING.md](https://github.com/SVijayB/Chat-Room-101/blob/master/.github/CONTRIBUTING.md) before sending us Pull requests. 

Also, thanks for contributing to Open-source!

## License 

Chat-Room-101 is under The MIT License. Read the [LICENSE](https://github.com/SVijayB/Chat-Room-101/blob/master/LICENSE) file for more information.
