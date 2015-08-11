click.py
This is very simple social engineering tool to verify if the users are still clicking exe's attached in anonymous emails etc.This can be use for social engineering test with out harming users or business.

Click.py is just a script so to make it work we need to make it as an exe by using pyinstaller tool(there is an -F -w for making the exe run in background) once  exe has created then we  can send it as an email attachment or downloadable via a url, as soon as the users click on the exe mongodb database will be feed with IP,hostname and username information(we can skip hostname or username based on the policy).

 If the mongoDB server sits in an external network then we can change the default mongoDB port number from 27017 to 80 or 443(normally these ports(80/443) are open by firewall for internet usage) or use NAT to hide.
 
 If there are any questions related to the this please contact me on "sreeju_kc@hotmail.com"
 
 Thanks
 Sreejith
