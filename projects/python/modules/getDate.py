import jdatetime
def getdate(text):
    user_input = input(text)
    try:
        jdatetime.datetime.strptime(user_input ,"%Y/%m/%d %H:%M")
        return user_input
    except:
        print("the format of date you have entered is wrong")
        return getdate(text)