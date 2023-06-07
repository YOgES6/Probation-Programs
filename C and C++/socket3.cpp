#include <iostream>
#include <string>
#include <sys/socket.h>
static bool port_is_open(const std::string& address, int port)
{
    return (TcpSocket().connect(address, port) == Socket::Done);
}

int main()
{
    int num;
    std::cout<<"Enter the port number";
    std::cin>>num;
    if (port_is_open("localhost", num))
        std::cout << "Opened" << std::endl;
    else
      std::cout << "Not opnened" << std::endl;
    return 0;
}
