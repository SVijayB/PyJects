# Chat-Room-101
<p align="center">
    <img src="assets/Logo.png" alt="Logo" border="0">
    <br>A Simple GUI based Chat Room Application.
</p>

---

## Motivation

This application was built to create a simple and easy to use interface for sending and receiving messages.

This application works on TCP connections made between devices over the internet.
Hence, messages are sent and recieved securely.

## Usage

<p align="center">
    <a href="https://github.com/SVijayB/Chat-Room-101"><img src="assets/SS.PNG" alt="Logo" border="0"></a>
</p>

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