from nltk.chat.util import Chat,reflections  

pairs = [
    ["(Hello Siri|Hi Siri)",["Hello,what's your name?"]],
    ['My name is (.*)', ["hi %1"]],
    ["(hi|hello|hey)",["hey there ","hello","how's you"]],
    ["(.*) your name",["My name is Siri"]],
    ["(how are you| how are you feelig)",["I'm doing well, thank you."]],
    ["(who created you | who is your creator| who made you)", ["I was created by brandon Jacobson,but we were all created by God"]],
    ["(what do you want to talk about)",["I don't know what do you want to talk about?, anything you want."]],
    ["(you are incredible| You're incredible)",[ "Thanks. So are you"]],
    ["are you a robot?",["Yes. I'm a digital assistant named Siri"]]
                             
]

chat = Chat(pairs, reflections)
chat.converse()