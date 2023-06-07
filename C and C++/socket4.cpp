#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
 
int main(int argc, char *argv[])
{
    int port;
    printf("Enter a port number to check ");
    scanf("%d",&port); 

    char hostname[] ="Aboves-Mac-mini.local";
    int sockfd;
    struct sockaddr_in serv_addr;
    struct hostent *server;
 
    server = gethostbyname(hostname);
 
   if (server == NULL)
   {
        fprintf(stderr,"ERROR, no such host\n");
        exit(0);
   }
 
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr,
         (char *)&serv_addr.sin_addr.s_addr,server->h_length);
 
    serv_addr.sin_port = htons(port);

 if (connect(sockfd,(struct sockaddr *) &serv_addr,sizeof(serv_addr)) < 0)
    {     
    printf("Port is closed\n\n");
    }
 else
    {
        printf("Port is active\n\n");
    }
    return 0;
}
