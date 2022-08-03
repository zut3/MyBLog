# Routes

## blog

+ "/" - home page 

## auth 
+ "/registration" - registrate new user and return special id for confirm email
> GET params: your email 
+ "/login" - confirm email 
> GET params: uuid, that you got in "/registartion" path