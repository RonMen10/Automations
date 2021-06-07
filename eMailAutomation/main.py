from inbox import*

if __name__ == "__main__":
    my_inbox = get_inbox()
    #print(my_inbox) 
    dic = {'subject': [], 'to':[], 'from':[], 'date':[], 'body':[]}
    for i in range(len(my_inbox)):
        probDictionary = my_inbox[i]
        dic['subject'].append(probDictionary['subject'])
        dic['to'].append(probDictionary['to'])
        dic['from'].append(probDictionary['from'])
        dic['date'].append(probDictionary['date'])
        dic['body'].append(probDictionary['body'])
    print(dic)
    for i in range(len(dic['body'])):
        with open("Output.txt", "a") as text_file:
            text_file.write(dic['body'][i])
    #myNotification = displayNotification("message","title","subtitle","Pop")
    myNotification = displayNotification("urgent",'Message from: {}'.format(dic['from'][0]),'Message: {}'.format(dic['body'][0][:15]),"Pop")