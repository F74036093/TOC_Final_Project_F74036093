from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    """def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'go to state1'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'go to state2'

    def on_enter_state1(self, update):
        update.message.reply_text("I'm entering state1")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("I'm entering state2")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')"""
    def is_going_to_ready(self, update):
        text = update.message.text
        return len(text) != 0

    def is_going_to_watch_monster(self, update):
        text = update.message.text
        return text == '卡通角色'
        #return True

    def is_going_to_watch_dog(self, update):
        text = update.message.text
        return text == '狗狗'
        #return False

    def is_going_to_watch_bird(self, update):
        text = update.message.text
        return text == '鳥兒'
        #return False

    def is_going_to_monster_sad(self, update):
        text = update.message.text
        return text == '皮卡丘'
        #return True

    def is_going_to_monster_happy(self, update):
        text = update.message.text
        return text == '小叮噹'
        #return False

    def is_going_to_dog_shibe(self, update):
        text = update.message.text
        return text == '站著的狗狗'
        #return False

    def is_going_to_dog_beagle(self, update):
        text = update.message.text
        return text == '跑步的狗狗'
        #return False

    def is_going_to_bird_seagull(self, update):
        text = update.message.text
        return text == '水鳥'
        #return False

    def is_going_to_user(self, update):
        text = update.message.text
        return text == '不想看了'
        #return False
    #def on_enter_user(self, update):
        #update.message.reply_text("")

    def on_exit_user(self, update):
        print('Leaving user')

    def on_enter_ready(self, update):
        update.message.reply_text("嗨～我這裡有一些漂亮的圖片！ 想看“卡通角色”還是“狗狗”或是“鳥兒”呢？")

    def on_exit_ready(self, update):
        print('Leaving ready')

    def on_enter_watch_monster(self, update):
        update.message.reply_text("想看“皮卡丘”還是“小叮噹”呢？如果突然不想看的話也可以輸入“不想看了”唷！")

    def on_exit_watch_monster(self, update):
        print('Leaving watch_monster')

    def on_enter_watch_dog(self, update):
        update.message.reply_text("想看“跑步的狗狗”還是“站著的狗狗”呢？如果突然不想看的話也可以輸入“不想看了”唷！")

    def on_exit_watch_dog(self, update):
        print('Leaving watch_dog')

    def on_enter_watch_bird(self, update):
        update.message.reply_text("現在只有一個“水鳥”的圖片耶，如果突然不想看的話也可以輸入“不想看了”唷！")

    def on_exit_watch_bird(self, update):
        print('Leaving watch_bird')

    def on_enter_monster_sad(self, update):
        update.message.reply_text("""
(｡◕‿‿◕｡)
""")
        update.message.reply_text("很可愛～不是嗎～想要看更多的話也歡迎唷～")
        self.go_back(update)

    def on_exit_monster_sad(self, update):
        print('Leaving watch_monster_sad')

    def on_enter_monster_happy(self, update):
        update.message.reply_text("""
┉┉╱▔▔▔▔▔▔▔▔╲
┉╱┉┉╱▔╲╱▔╲┉┉╲
╱┉╱▔▏▇▕▏▇▕▔╲┉╲
▏╱╲┉╲▂╭╮▂╱┉╱╲▕
▏▏━╭╮┉╰╯┉╭╮━▕▕
▏▏╱╰┳━┻┻━┳╯╲▕▕
▏▏┉┉┃╭━━╮┃┅┅▕▕
╲╲┉┉╰┻━━┻╯┉┉╱╱
┉╲╲▄▄▄▄▄▄▄▄▄▄▄╱╱
""")
        update.message.reply_text("很可愛～不是嗎～想要看更多的話也歡迎唷～")
        self.go_back(update)

    def on_exit_monster_happy(self, update):
        print('Leaving watch_monster_happy')

    def on_enter_dog_shibe(self, update):
        update.message.reply_text("""
┈┈┈┈┈┈┈┈┈┈┈┈┈
^◕◕^┈┈┈┈┈┈/┈┈
/_/\▄▄▄▄▄/┈┈┈
┈┈┈/\┈┈┈/\┈┈┈
┈┈/┈┈\┈/┈┈\┈┈
""")
        update.message.reply_text("很可愛～不是嗎～想要看更多的話也歡迎唷～")
        self.go_back(update)

    def on_exit_dog_shibe(self, update):
        print('Leaving dog_shibe')

    def on_enter_dog_beagle(self, update):
        update.message.reply_text("""
┈╱▏┈┈┈┈╱▔▔▔▔╲┈┈
┈▏▏┈┈┈┈▏╲▕▋▕▋▏┈
┈╲╲┈┈┈┈▏┈▏┈▔▔▔▆
┈┈╲▔▔▔▔╲╱┈╰┳┳┳╯
╲╱╲▏┈┈┈┈┈▕▔╰━╯┈
╲╲╱╱▔╱▔╲╲╲╲┈┈┈┈
┈╲╱╲╱┈┈┈╲╲▂╲▂┈┈
┈┈┈┈┈┈┈┈┈╲╱╲╱┈┈
""")
        update.message.reply_text("很可愛～不是嗎～想要看更多的話也歡迎唷～")
        self.go_back(update)

    def on_exit_dog_beagle(self, update):
        print('Leaving dog_beagle')

    def on_enter_bird_seagull(self, update):
        update.message.reply_text("""
````__
___(-o)>
\.<_.-)
.`———‘   
""")
        update.message.reply_text("很可愛～不是嗎～想要看更多的話也歡迎唷～")
        self.go_back(update)

    def on_exit_bird_seagull(self, update):
        print('Leaving bird_seagull')