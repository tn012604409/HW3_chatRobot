from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_menu(self, update):
        text = update.message.text
        return text.lower() == 'menu'

    def is_going_to_chinese(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_Italy(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_Thiland(self, update):
        text = update.message.text
        return text.lower() == '3'
    def is_going_to_USA(self, update):
        text = update.message.text
        return text.lower() == '4'

    def is_going_to_fry(self, update):
        text = update.message.text
        return text.lower() == 'a'
    def is_going_to_saute(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_spring(self, update):
        text = update.message.text
        return text.lower() == '1st'
    def is_going_to_yam(self, update):
        text = update.message.text
        return text.lower() == '2nd'

    def is_going_to_beef(self, update):
        text = update.message.text
        return text.lower() == '1st'
    def is_going_to_egg(self, update):
        text = update.message.text
        return text.lower() == '2nd'

    def is_going_to_spaghetti(self, update):
        text = update.message.text
        return text.lower() == 'a'
    def is_going_to_stew(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_tomato(self, update):
        text = update.message.text
        return text.lower() == '1st'
    def is_going_to_butter(self, update):
        text = update.message.text
        return text.lower() == '2nd'

    def is_going_to_wine(self, update):
        text = update.message.text
        return text.lower() == '1st'
    def is_going_to_sea(self, update):
        text = update.message.text
        return text.lower() == '2nd'

    def is_going_to_squid(self, update):
        text = update.message.text
        return text.lower() == 'a'
    def is_going_to_thaiNoodle(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_chicken(self, update):
        text = update.message.text
        return text.lower() == 'a'
    def is_going_to_Ham(self, update):
        text = update.message.text
        return text.lower() == 'b'


    def on_enter_menu(self, update):
        print('enter menu')
        update.message.reply_text("請輸入 1 中式，2 義式，3 泰式，4 美式")
        self.advance(update)
    def on_exit_menu(self, update):
        print('Leaving menu')

    def on_enter_chinese(self, update):
        print('enter chinese')
        update.message.reply_text("請輸入  a 油炸， b 清炒")
        self.advance(update)
    def on_exit_chinese(self, update):
        print('Leaving chinese')

    def on_enter_Italy(self, update):
        print('enter Italy')
        update.message.reply_text("請輸入 a 義大利麵，b 燉飯")
        self.advance(update)
    def on_exit_Italy(self, update):
        print('Leaving Italy')

    def on_enter_Thiland(self, update):
        print('enter Thiland')
        update.message.reply_text("請輸入 a 涼拌中捲，b 炒河粉")
        self.advance(update)
    def on_exit_Thiland(self, update):
        print('Leaving Thiland')

    def on_enter_USA(self, update):
        print('enter USA')
        update.message.reply_text("請輸入 a 炸雞，b 漢堡")
        self.advance(update)
    def on_exit_USA(self, update):
        print('Leaving USA')

    def on_enter_fry(self, update):
        print('enter fry')
        update.message.reply_text("請輸入 1st 炸春捲，2nd 炸地瓜")
        self.advance(update)
    def on_exit_fry(self, update):
        print('Leaving fry')

    def on_enter_saute(self, update):
        print('enter saute')
        update.message.reply_text("請輸入 1st 蔥爆牛，2nd 蝦仁炒蛋")
        self.advance(update)
    def on_exit_saute(self, update):
        print('Leaving saute')

    def on_enter_spring(self, update):
        print('enter spring')
        update.message.reply_text("食材:\n   春捲皮 1斤\n   韭菜 1斤\n   豬絞肉 1斤\n   冬粉 3小把\n   豆芽菜 1斤\n   鹽 2茶匙\n   白胡椒粉 適量\n   麵粉 兩大匙\n   水 2大匙\nSTEP1:  冬粉泡水後切段、麵粉和水調勻備用。韭菜切段後，加入半茶匙的鹽，稍微抓一下，並靜置約15分鐘讓其出水 \nSTEP2:  韭菜出水後再稍微抓捏一下瀝出水分倒掉，再加入其他配料，以及鹽和白胡椒粉調味，並用手攪拌均勻即完成內餡 \nSTEP3:  開始包春捲囉！拿一張春捲皮，取適量內餡放在中間偏下的位置 \nSTEP4:  兩側的餅皮在往內收時，讓其稍微呈梯形，包起來會比較漂亮～ \nSTEP5:  捲起來到剩下一些餅皮後，沾些麵糊水塗在餅皮上，把春捲給黏起來  \nSTEP6:  春捲就這樣完成囉！其實包真的包很快，一下子就包完了，一斤的春捲皮大約可以包26條喔！ \nSTEP7:  熱油鍋炸春捲，炸至金黃即可起鍋～  \n  ")
        self.go_back(update)
    def on_exit_spring(self, update):
        print('Leaving spring')

    def on_enter_yam(self, update):
        print('enter yam')
        update.message.reply_text("食材:\n    水林黃地瓜 2個 \n    麥芽糖 2湯匙 \nSTEP1:  地瓜清洗後，切薄片  \nSTEP2:  泡水後，晾乾。 \nSTEP3:  下油鍋，冷油溫火炸到成金黃色，起鍋還是軟軟的，起鍋待涼。 \nSTEP4:  回溫就變脆了哦  \nSTEP5:  乾淨鍋加入麥芽炒熱、，，倒入脆片，完成囉… 免排隊的台東地瓜酥   \n")
        self.go_back(update)
    def on_exit_yam(self, update):
        print('Leaving yam')

    def on_enter_beef(self, update):
        print('enter beef')
        update.message.reply_text("食材:\n    嫩牛肉絲 300克 \n    蔥(切段) 6到8根 \n    醬油 一小匙 \n    水 一小匙 \n    胡椒粉 少許 \n    太白粉 少許 \n    糖 一點點 \n    醬油膏(醬油也可) 一匙\n    糖 一點點\n    水 三匙\n    胡椒粉 一點點\n    黑胡椒 一點點\n    沙拉油(過油用) 六匙\nSTEP1:  把醬油 水 胡椒粉 太白粉 糖 抓醃好 要用手用力抓幾下 讓調味料入到牛肉裡喔 然後靜置一下下  \nSTEP2:  一把蔥 切段 用盤子裝 蔥白和蔥綠要分一下 等下下鍋時間不同  \nSTEP3:  放入六大匙的油 中溫時牛肉放入過一下 不要過太久 這可以保持牛肉的嫩度 瀝乾油(剩下的油還很乾淨 可以再利用 不要倒掉喔)  \nSTEP4:  加蔥爆炒 用原來過油的鍋子炒 就不用再加油 因為鍋子很油 先炒蔥白 炒到有微微香氣再加上蔥綠 炒香 加點水  \nSTEP5:  把瀝乾的牛肉絲加入 稍微拌炒   \nSTEP6:  加入調味料 (醬油膏 糖 胡椒粉 黑胡椒) 炒一下  \nSTEP7:  聞到香氣 起鍋就完成了   \n  ")
        self.go_back(update)
    def on_exit_beef(self, update):
        print('Leaving beef')

    def on_enter_egg(self, update):
        print('enter egg')
        update.message.reply_text("食材:\n     蝦仁 10隻  \n    蛋 2個  \n     蔥花 些許 \nSTEP1:  蝦仁退冰洗淨擦乾，用米酒、白胡椒、鈦白粉抓一下，放5分鐘  \nSTEP2:  中火溫油煎蝦仁，兩面都變色後撈起 \nSTEP3:  打蛋加一點水、鹽、蔥花打散，小火原鍋加一點油，蛋倒進去之後用筷子從外向內畫圓，蛋5分熟後放入1，到蛋8分熟就可以關火了！  \n")
        self.go_back(update)
    def on_exit_egg(self, update):
        print('Leaving egg')

    def on_enter_spaghetti(self, update):
        print('enter spaghetti')
        update.message.reply_text("請輸入 1st  番茄義大利麵，2nd 奶油義大利麵")
        self.advance(update)
    def on_exit_spaghetti(self, update):
        print('Leaving spaghetti')

    def on_enter_stew(self, update):
        print('enter stew')
        update.message.reply_text("請輸入 1st  紅酒燉飯，2nd 西班牙海鮮燉飯")
        self.advance(update)
    def on_exit_stew(self, update):
        print('Leaving stew')

    def on_enter_tomato(self, update):
        print('enter tomato')
        update.message.reply_text("食材:\n    番茄醬 約110g\n    瀝乾鮪魚（油/水） 60g\n    水 2大匙\n    蒜頭 1-2瓣\n    橄欖油 適量\n    義式香料 適量\n    黑胡椒 適量\n    義大利麵一人份 約65g\n    鹽巴 適量\n    水 適量\nSTEP1:  水+鹽，並將水煮滾後，下義大利麵（依照包裝指示煮熟）   \nSTEP2:  同時 放入橄欖油+蒜末以中小火爆香並翻炒（約4-5分鐘）  \nSTEP3:  加入番茄醬+水放入鍋中翻炒 再加入適量義式香料及黑胡椒 均勻即可   \nSTEP4:  放入鮪魚拌炒 約2-3分鐘\nSTEP5:  加入已熟的義大利麵拌炒1分鐘    \n")
        self.go_back(update)
    def on_exit_tomato(self, update):
        print('Leaving tomato')

    def on_enter_butter(self, update):
        print('enter butter')
        update.message.reply_text("食材:\n     義大利麵 2人份 \n     培根 4片 \n     蘑菇 3-4個 \n     蒜頭 2-3粒 \n     洋蔥 半個 \n     蛋黃 2個 \n     鮮奶油 200ml \nSTEP1:  先用深鍋加水滾後加鹽和橄欖油加入麵條按包裝指示時間煮熟撈起後加點橄欖油拌勻 \nSTEP2:  培根切小塊放入平底鍋（不需加油培根本身會出油）乾煎至有點焦焦取出 剩餘的油放入蒜頭煎香加入洋蔥拌炒至洋蔥略為透明色再加入切好的蘑菇續炒加鹽和少許黑胡椒粒拌炒再加入煮好的麵和煮麵的水約2湯匙繼續拌炒入味 \nSTEP3:  蛋黃2顆加上鮮奶油調和成蛋黃醬汁（煮麵時可先準備 \nSTEP4:  麵拌勻後關火將蛋黃液慢慢倒入麵中慢慢拌勻若太乾可再加些煮麵水即可 \nSTEP5:  將剛煎好的培根放在麵上灑上一些起司粉和洋香菜就可食用囉    \n")
        self.go_back(update)
    def on_exit_butter(self, update):
        print('Leaving butter')

    def on_enter_wine(self, update):
        print('enter wine')
        update.message.reply_text("食材:\n     義大米 2杯(量米杯)\n     洋蔥 1顆(大)\n     蘑菇 2盒\n     蒜頭 6-8瓣\n      新鮮巴西里 10g \n     無骨牛小排 1盒\n     紅酒 100ml\n     雞高湯 1400ml\n     研磨黑胡椒粒 適量\n     義大利綜合香料 適量\n     二砂糖 1/4大匙\n     鹽 1/4大匙\n     無鹽奶油 20g\nSTEP1:  將蒜頭/洋蔥/新鮮巴西里切末，蘑菇切片，無骨牛小排切小塊(ㄧ口入嘴的大小)。   \nSTEP2:  冷鍋時放入蒜末/洋蔥末，再加入適量的橄欖油後開中火，將蒜末/洋蔥末炒香後，再放入蘑菇ㄧ起炒香。   \nSTEP3:  承步驟2. 同時取另ㄧ只牛排鍋(or平底鍋)，開中火先熱鍋後，放入無骨牛小排，將牛小排煎出焦香味及稍微上色後，就先夾起放ㄧ旁備用。 * 勿將牛小排煎過老哦！   \nSTEP4:  將ㄧ旁備用牛小排加入鍋中，和蒜末/洋蔥末/蘑菇ㄧ起炒香ㄧ下。   \nSTEP5:  接著，放入義大利米及倒入橄欖油(橄欖油瓶轉ㄧ圈的量)拌ㄧ拌，讓義大利米平均都吸收到橄欖油後，再丟入無鹽奶油，讓鍋中所有食材全吸收到奶油香氣後再倒入紅酒，待酒精揮發後加入ㄧ~二大湯匙量的高湯，要ㄧ直拌炒至高湯汁快收乾。 *此步驟高湯是加ㄧ大湯匙的量，不是全部份量的高湯哦！*   \nSTEP6:  要ㄧ直不斷重複加高湯的步驟，當高湯用至ㄧ半的量時，此時(米吸取高湯快收乾時)，加入巴西里/義大利綜合香料/研磨黑胡粒/二砂糖/(鹽)後，再重覆加高湯步驟，直至義大利米心的口感是自己想要的感覺即可停止，不再加入高湯，紅酒牛小排燉飯大至完成。 * 若是使用雞湯塊煮成的高湯，此步驟不需再加鹽。*   \nSTEP7:  最後，將完成的燉飯呈盤後加上松露醬，松露紅酒牛小排燉飯就完成啦！   \n ")
        self.go_back(update)
    def on_exit_wine(self, update):
        print('Leaving wine')

    def on_enter_sea(self, update):
        print('enter sea')
        update.message.reply_text("食材:\n     西班牙燉飯米 2杯\n     蘆筍 若干\n     洋蔥 半顆\n     大蒜 2顆\n     雞高湯 600ml\n     番茄 1顆\n     黃檸檬 1顆\n     蝦子 適量\n     透抽 適量\n     淡菜 適量\n     煙燻紅椒粉 適量\n     橄欖油 適量\n     鹽 適量\n     黑胡椒 適量\n     番紅花 適量\n     白酒 100ml\n     巴西里 半碗\nSTEP1:  需切丁備料的食材有：洋蔥、大蒜、番茄。  \nSTEP2:  將鍋子預熱後放入橄欖油，先將洋蔥、大蒜下鍋爆香直到洋蔥變至透明色，再以適量黑胡椒及鹽調味。   \nSTEP3:  放入番茄、蘆筍並加入適量煙燻紅椒粉拌炒均勻。   \nSTEP4:  加入雞高湯、燉飯米、番紅花、白酒後，中大火燉煮15-20分鐘。   \nSTEP5:  鋪上準備好的海鮮食材，再加蓋悶煮5-10分鐘，起鍋時撒上巴西里及切片檸檬即可上桌。  \n")
        self.go_back(update)
    def on_exit_sea(self, update):
        print('Leaving sea')

    def on_enter_squid(self, update):
        print('enter squid')
        update.message.reply_text("食材:\n     中卷（透抽） 1-2尾\n     紫洋蔥 0.5顆\n     紅蕃茄(牛番茄) 1顆\n     小黃瓜 1條\n     泰式甜雞醬  2大匙\n     椒麻醬汁\n     淬釀醬油露 0.5-1大匙\n     檸檬(汁) 0.5顆(1.5大匙\n     烏醋 1茶匙\n     糖 1茶匙\n     蒜頭 3瓣\n     辣椒 1條\n     香菜 1-2顆\n     香油或麻油 1茶匙\nSTEP1:  準備所有食材，清理與清洗之。  \nSTEP2:  小黃瓜切圓薄片，紫洋蔥切細絲，蕃茄切丁，透抽切花刀，蒜頭、辣椒、香菜切末。  \nSTEP3:  洋蔥以適量冰開水浸泡約10分鐘，完成後瀝乾水份。  \nSTEP4:  小黃瓜以少許鹽抓捏一下，醃漬約10分鐘去草腥味，倒除湯汁檸乾。  \nSTEP5:  起鍋內鍋放入適量的水，開中火煮滾後，放入中捲汆燙，花邊捲起，即可關火， 再放置約1分鐘熟成即可。 \nSTEP6:  撈起中卷放入冰開水中冷卻，再撈起瀝乾水份。\nSTEP7:  調椒麻醬汁:取一小碗，將所有椒麻醬汁食材加入(蒜頭、辣椒、香菜各加一半的量，其他全加)，攪拌均勻即可。 (可試味道:依自己喜愛調整鹹、酸、甜度，可由醬油、檸檬汁、糖做適度的調 整，喜愛魚露者亦可加入拌之)  \nSTEP8:  取一中碗，將前處理好的小黃瓜、紫洋蔥、蕃茄及另一半量的蒜頭、辣椒、香菜加入泰式甜雞醬攪拌均勻。   \nSTEP9:  攪拌好的食材鋪於盤底，擺上熟成的中卷。   \nSTEP10:  再淋上調製好的椒麻醬汁即完成。 \n       ")
        self.go_back(update)
    def on_exit_squid(self, update):
        print('Leaving squid')

    def on_enter_thaiNoodle(self, update):
        print('enter thaiNoodle')
        update.message.reply_text("食材:\n     花生 一把\n     河粉 3-4片\n     蛋 2顆\n     蝦子 6-8隻\n     雞胸肉 一片\n     小蝦米 6-8顆\n     菜脯 適量\n     豆芽菜 適量\n     甜椒 適量\n     豆乾 2塊\n     洋蔥 半顆\n     紅蘿蔔 適量\n     菇類 適量\n     魚露 適量\n     九層塔 適量\n     泰式河粉醬\n     乾羅望子 50g\n     溫開水 75ml\n     棕梠糖/椰糖 2湯匙\n     番茄醬 1湯匙\n     鹽 1/4\nSTEP1:  首先先把材料都先切好，盡量都切差不多大小。洋蔥 青椒 紅蘿蔔 豆乾 菇類 蔥 雞胸肉 都切丁，小蝦米泡水 九層塔洗乾淨 蝦子小番茄剖半（有些料沒照到請不要介意～）   \nSTEP2:  把乾羅望子放麵粉篩網上泡水後用手先抓捏把汁液擠出來，之後用湯匙的背面把汁液擠下去，汁液擠的差不多了就可以把羅望子籽丟掉，再加入椰糖攪拌 \nSTEP3:  首先先把板條撥開，這個步驟很重要一定要先撥開，不然你丟進去煮他不會自己散開就會全部黏再一起，要先把一整片的粄條攤開在切成想要的粗度，加一點點香油或芝麻油辦一辦，再放到熱鍋裡先稍微乾炒，炒到粄條沒那麼硬了就可以先關火放旁邊備用  \nSTEP4:  把花生先稍微乾煎一下，讓香氣出來 \nSTEP5:  花生煎好後就可以搗一搗，沒有杵臼的話就放在塑膠袋裡用桿麵棍就酒瓶敲一敲  \nSTEP6:  再來就是煎蛋 ,就是起鍋熱油煎兩顆蛋，煎好不要太熟就撈起來先備用 \nSTEP7:  用剛剛煎蛋的同鍋，再加一點點油 先把切碎的小蝦米丟進去爆香一下   \nSTEP8:  接著切丁的 洋蔥 青椒 紅蘿蔔 豆乾 全部加進去（這是懶人男人的做法）（是我的話就會先洋蔥炒到快透明在加豆乾奸相之後才加青椒跟紅蘿蔔）（但是我不會說他錯的）（不然以後就沒得吃了顆顆）  \nSTEP9:  炒到差不多之後就把切丁的雞肉放進來 \nSTEP10:  到雞肉六七分熟後加入菇類和番茄  \nSTEP11:  到番茄皮開始有點皺了菇類開始出水，把剛炒過的板條加進去，再把泡蝦米的水也一起放進去   \nSTEP12:  稍微攪拌一下再加入剛煎好的蛋   \nSTEP13:  最後加入最重要的Pad Thai醬汁一起拌炒 \nSTEP14:  拌炒到醬都均勻了且板條都熟了（會變得更軟），加入蔥綠 \nSTEP15:  最後關火前把九層塔葉放進去，攪拌幾秒就關火就可以起鍋拉～ \nSTEP16:  要吃的時候撒上剛搗碎的花生，再淋上新鮮檸檬汁～ \n")
        self.go_back(update)
    def on_exit_thaiNoodle(self, update):
        print('Leaving thaiNoodle')

    def on_enter_chicken(self, update):
        print('enter chicken')
        update.message.reply_text("食材:\n     雞翅 9隻\n     洋蔥粉(可省) 1.5小匙\n     蒜末 1小匙\n     匈牙利紅椒粉 1.5大匙\n     鹽巴 少許\n     黑胡椒 少許\n     白(米)酒 1大匙\n     中筋麵粉 3大匙\n     醬汁\n     無鹽奶油 60g\n     美式辣醬 5大匙\n     番茄醬 3大匙\n     白酒醋(白醋) 1.5大匙\n     蒜末 1小匙\n     黑胡椒 少許\n     鹽巴 少許\nSTEP1:  首先將雞翅切好、擦乾後，與麵粉以外的調味料均勻混合醃製至少45分鐘。 \nSTEP2:  接著取一個袋子，將雞翅與麵粉倒入袋中，搖晃袋子讓雞翅均勻沾裹麵粉，再來將雞翅放入烤箱用200度烤約30分鐘。  \nSTEP3:  取一醬汁鍋，先將奶油下鍋融化後，將醬汁其餘的材料下鍋煮均勻後備用。  \nSTEP4:  最後等雞翅烤好後和步驟3的醬汁均勻混合後就完成了。 \n")
        self.go_back(update)
    def on_exit_chicken(self, update):
        print('Leaving chicken')

    def on_enter_Ham(self, update):
        print('enter Ham')
        update.message.reply_text("食材:\n     牛絞肉(脂肪>20%) 250g\n     洋蔥切末 1/4顆\n     大蒜切末 1~2瓣\n     胡蘿蔔切細末 1/2根\n     雞蛋 1/2顆\n     伍斯特醬(梅林辣醬油) 2茶匙\n     黃芥末醬 1茶匙\n     巴西里葉末 少許\n     (配料)洋蔥圈 1/4顆\n     (配料)牛番茄切片 1顆\n     (配料)起士片 2片\n     漢堡醬料\n     酸黃瓜 少許\n     番茄醬 2大匙\n     黃芥末醬 1大匙\n     黑胡椒 少許\n     鹽 少許\n     義大利香料 少許\n     伍斯特醬(梅林辣醬油) 1湯匙\nSTEP1:  起油鍋，逐步加入洋蔥末、蒜末與胡蘿蔔細末炒至軟爛備用，讓食材甜味充分釋放。  \nSTEP2:  取攪拌碗，將已退冰完成的牛絞肉放入，加入雞蛋半顆（增添雞蛋香味）、鹽少許、黑胡椒少許與伍斯特醬油2茶匙、黃芥末醬1茶匙。\nSTEP3:  將步驟1炒軟的食材加入攪拌盆，並加入少許巴西里葉末。 \nSTEP4:  用雙手將食材攪拌均勻，為了保持肉排的水分與口感，請不要摔打肉團，簡單的整理好形狀即可。（可加入少許麵包粉，讓肉排更容易塑形） \nSTEP5:  以雙手將肉排捏成圓餅狀，並用指頭在肉排中央壓出凹陷，待會在煎肉排時，受熱會更為均勻。 \nSTEP6:  取鑄鐵煎盤(或平底鍋)，加熱至高溫，加入少許牛油後，放上肉排，每面煎約5分鐘即可。可於此同時準備醬料（將「漢堡醬料」中食材攪拌均勻即可）並加熱漢堡麵包。漢堡排翻面後，將起士片置於漢堡排上，並同時將洋蔥圈、番茄片置於鐵板上烤至軟嫩，牛肉排煎熟後，可將全部食材起鍋、組合。\nSTEP7:  漢堡排翻面後，將起士片置於漢堡排上，並同時將洋蔥圈、番茄片置於鐵板上烤至軟嫩，牛肉排煎熟後，可將全部食材起鍋、組合。   \nSTEP8:  健康無添加的美式牛肉漢堡，完成！ ")
        self.go_back(update)
    def on_exit_Ham(self, update):
        print('Leaving Ham')
    






















