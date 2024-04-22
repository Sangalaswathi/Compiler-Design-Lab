#include<stdio.h>

#include<ctype.h>

#include<string.h>

int main()

{

        FILE *ip, *op;

        int l=1; int t=0; int j=0; int i,flag;

        char ch,str[20];

        ip = fopen("ip.txt","r");

        op = fopen("op.txt","w");

        char keyword[30][30] = {"int","main","if","else","do","while", "return", "include"};

        fprintf(op,"Line no.   \t Token no.          \t Token       \t Lexeme\n\n");

        while(!feof(ip))

        {

                i=0; flag=0; ch=fgetc(ip);

                if( ch=='+' || ch== '-' || ch=='*' || ch=='/' )

                {

                        fprintf(op,"%7d\t\t %7d\t\t Operator\t %7c\n",l,t,ch);

                        t++;

                }

                else if( ch==';' || ch=='{' || ch=='}' || ch=='(' || ch==')' || ch=='?' || ch=='@' || ch=='!' || ch=='%')

                {

                        fprintf(op,"%7d\t\t %7d\t\t Special symbol\t %7c\n",l,t,ch);

                        t++;

                }

                else if(isdigit(ch))

                {

                        fprintf(op,"%7d\t\t %7d\t\t Digit\t\t %7c\n",l,t,ch);

                        t++;

                }

                else if(isalpha(ch))

                {

                        str[i]=ch;

                        i++;

                        ch=fgetc(ip);

                        while(isalnum(ch) && ch!=' ')

                        {

                                str[i]=ch;

                                i++;

                                ch=fgetc(ip);

                        }

                        str[i]='\0';

                        for(j=0;j<=8;j++)

                       {

                                if(strcmp(str,keyword[j])==0)

                                {

                                        flag=1;

                                        break;

                                }

                        }

                        if(flag==1)

                        {

                                fprintf(op,"%7d\t\t %7d\t\t Keyword\t %7s\n",l,t,str);

                                t++;

                        }

                        else

                        {

                                fprintf(op,"%7d\t\t %7d\t\t Identifier\t %7s\n",l,t,str);

                                t++;

                        }

                }

                else if(ch=='\n')

                {

 

                        l++;

                }

        }

        fclose(ip);

        fclose(op);

        return 0;

}