#include <netdb.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <sys/socket.h>
#include <unistd.h>
#define MAX 80
#define PORT 61000
      
void func(int connfd)
{
       char buff[MAX];
       int n;
       for (;;) 
       {
       bzero(buff, MAX);
   
       read(connfd, buff, sizeof(buff));
       printf("From client : %s\n\t To client : ", buff);
       bzero(buff, MAX);
       n = 0;
       while ((buff[n++] = getchar()) != '\n')
        write(connfd, buff, sizeof(buff));
       if (strncmp(buff, "exit", 20) == 0) 
        {
            printf("Server Exit...\n");
            break;
        }
        }
}


int main()
{

	int server_fd, new_socket, len;
	struct sockaddr_in address;
	char * hello;
        printf("Enter the message to client: "); 
        scanf("%c",&hello);
        int opt = 1;
	int addrlen = sizeof(address);
	char buffer[1024] = { 0 };
              
	if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		perror("socket failed");
		exit(EXIT_FAILURE);
	}

	if (setsockopt(server_fd, SOL_SOCKET,SO_REUSEPORT, &opt,
				sizeof(opt))) {
		perror("setsockopt");
		exit(EXIT_FAILURE);
	}
	address.sin_family = AF_INET;
	address.sin_addr.s_addr = INADDR_ANY;
	address.sin_port = htons(PORT);

	if (bind(server_fd, (struct sockaddr*)&address,
			sizeof(address))
		< 0) {
		perror("bind failed");
		exit(EXIT_FAILURE);
	}
	if (listen(server_fd, 3) < 0) {
		perror("listen");
		exit(EXIT_FAILURE);
	}
	if ((new_socket	= accept(server_fd, (struct sockaddr*)&address,
				(socklen_t*)&addrlen))< 0)
        {
		perror("accept");
		exit(EXIT_FAILURE);
	}
        func(new_socket); 
        close(new_socket);
}
