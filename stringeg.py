# username =input("Enter your name")
# print(username)
# # for ch in username:
# #     print(ch)
# print(username.upper())
# print(username)
# print(username[0])
# # username = "Maria"
# # username[0]="K"   this will throw err
# # print(count(username))
# print(username.lower())
# print(len(username))
# vcount=0
# for ch in username:
#     if(ch in "aeiouAEIOU"):
#         vcount=vcount+1
# print(f"no of vowels in {username} is {vcount}")
# ---------------------------------
# msg = """Hello world how are you today , today we are working with string ,
# you will learn string today  """
# print(msg *3)
# print(msg[5])
# print(msg[5:])
# print(msg[:8])
# print(msg[5:15])
# print(msg)
# print(msg.strip())
# print(msg.lstrip())
# print(msg.rstrip())
# -----------------------
# msg = msg.strip()
# print(msg.split(" "))
# word = input("enter any word")
# you_count=0
# for e in msg.split(" "):
#     if((e.upper())==(word.upper())):
#         you_count= you_count+1
# print(you_count, " no of times ",word," comes in given string")
# ----------------------
# msg = msg.replace("Hello","hi")
# print(msg)
# ----------------------
pwd = "abcde123"
print(pwd.isalnum())
print(pwd.isnumeric())
print(pwd.isalpha())