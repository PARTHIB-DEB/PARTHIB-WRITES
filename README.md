# PARTHIB-WRITES (Personal Blog) (Feb 6,2024 - Feb 29,2024 )
- 🖋️ This is My First Full Stack Project Using Django and TailwindCSS. Its V1 was created during Feb-2023. But at that stage It was Not so much featureful 😕.
  
- 🌝 So I thought to recreate the project.

- 🌟 Let's have a look on the feature differences.

- Video : [video](https://drive.google.com/file/d/1xLktMmcWJxG_LZz_WccKFYuVuBQQFHHf/view?usp=sharing)
  
## Features ⚡⚡
- ### User Authentication ✔️
  The primary Goal of this project is to make it safe and less vulnerable from the attacks of anonymous / Unauthenticated Users. So I created this module - by taking help 
  of **Django Authentication System** . Roughly The AUTH game in Django can be depicted like that - There are certain ```Groups``` of users , who have some categories of       ```permissions``` , bascially they are two different ```models``` or SQL Relations who maintain ```M-2-M``` relationship among them. Now ```Users``` are one of the Groups    who have some permissions over the app - by default set by django. Now this ```Users``` is also a Model , which Got inherited from ```AbstractUser``` Model, which furthur    inherited from ```AbstractBaseUser``` Model. Here I have Just Used the ```AbstractUser``` Model , and created my own user model by changing some of the method Definitions
  little bit. **Check out inside ```users``` 📁**

- ### Django Forms EveryWhere ✔️
  Although Previously I did the ```Create-Read-Update-Delete``` operations on blogs , but there I did not take the help of ```Django Forms```. I  fetched the raw data 
  from ```request.POST``` dictionary , which might have caused vulnerability. So here for all set of operations , I used this feature provided by django.

- ### Postgresql Database ✔️
  Databases are crucial choices and Django gives native support for couple of good SQL databases - Postgres is one of them. Its a good Object-Oriented Database , have safety
  safety checking technoques like ```Row Security Policies```.  So I switched to this database

- ### Own Django + Tailwind Setup ✔️
  In V1 , I used a readymade packadge , which was not so developer-friendly . So I saw How they made the combination of two different servers and do that manually. Basically
  I applied ```TailwindCss-CLI``` with ```Django``` **(There is one tutorial in my github on this topic , can check out)**. **❗❗ This Way is not recommended for bigger projects**

- ### Emailing the User ✔️
  Although The code for email is perfect . But as I am using my personal email as sender. so the recever's gmail is not allowing , because its not an email of a company. simple any unsafe app , not having any domain can't send email using the gmail service

- ### Writing TestCases by Pytest ✔️
  So , I have written the testcases for both **users** and **blogs** . I declared a **conftest** file, where I created 2 **Class Based Test configurations** individually. Then I used them in my respective test-files.

## How to download this project :

```bash
  git clone https://github.com/PARTHIB-DEB/PERSONAL-BLOG.git
```

```bash
  python -m pip install -r requirements.txt

  or

  python3 -m pip install -r requirements.txt

  or

  pip install -r requirements.txt
```
**Although Upgrade Your Django Version , whenever you download it.**
