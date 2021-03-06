# -*- coding: utf-8 -*-
'''
Created on Nov 10, 2017

@author: Taoheng
'''

import itchat, time
import datetime as dt
from apscheduler.schedulers.background import BackgroundScheduler
import random
# 一些备选问候语
greetList = ['想你的时候有的甜，哭泣时想你那淡淡的体香抱着我让心灵有属于我的寄托。',
'花自飘零水自流，一种相思，两处闲愁。此情无计可消除，才下眉头，却上心头。',
'爱过就无悔，虽然痛彻心扉过，但想起你的柔情，在飘雪的日子里，也会看到春天，想你。',
'假如你的寿命是年，那我希望自己活到岁的前一天，因为那样的我的生命中每一天都有你…',
'想你，是一种美丽的忧伤的甜蜜的惆怅，心里面，却是一种用任何语言也无法表达的温馨。',
'爱上你的微笑，爱上你的善良，也爱上你的天真可爱，你就是我命中注定的另一半，爱你……',
'与君相思意，几人解风情？伴君听雪语，何人会其明？不求天伦之乐，但愿相惜相守度此生！',
'两情若是长久时，又岂在朝朝暮暮。亲爱的宝贝，我不能常陪伴着你，但我和你的心永远在一起。',
'黄昏中总有不变的等候，晚风中总有永恒的期待，寂寞时总有孤独的身影，想你时总有想思的泪滴。',
'爱到天荒地老，海枯石烂，天地合一，这些都是爱情的谎言，我只要牵着你的手一直到生命最后一秒！',
'我思念你，我喜欢你，我爱你，你是我最亲爱的人。希望你能把握现在，永不放弃，最爱你的人是我！',
'很想你，我不知道现在这还意味着什么，只是明白，我将永失我爱。但我会真心祝福你，我曾经的宝宝。',
'不管是在未知的天之涯，海之角，我希望将来老到掉牙的那一天，陪我牵手看夕阳的看云舒云卷的还是你。',
'我一生中最幸运的两件事：一件是时间终于将我对你的爱消耗殆尽；一件是很久很久以前有一天，我遇见你。',
'分分秒秒显得清澈又珍贵，只有你才能给我这种感觉，不管心多疲倦，梦想还有多远，有你陪伴一切都无所谓！',
'当你孤独时，我从黑暗中来到你的身边，斩碎那让你不安的孤独；当你不再孤独时，我会回到那无尽的黑暗中去。',
'我一直都知道我很爱你，但是我没有说出来，那是因为我不能不想你。现在我说了，是因为我很在乎你。知道吗？',
'给我一个时间说爱，用我的心化成星星，填满你寂寞的夜里，从来不曾有过这样的感觉，我却渴望拥有美丽的永远。',
'你笑了，我的天空放晴；你恼了，我的天空多云；你的一举一动，左右我的心情；。亲爱的，我在蜜罐里思念着你！',
'如果决定离开一个人，行动要快一点，快刀斩乱麻；如果决定爱上一个人，时间拉长一点，看清楚是否真的适合你。',
'我心怀天地，只因天地间有你惑人的笑；醉人的眼；天籁般的音；动人的身影；如光之精灵在清晨的柔光下轻歌曼舞。',
'流水是白云的影子，月亮是太阳的影子，黑夜是白天的影子，痛苦是爱的影子。不求你做我的影子，甘愿我做你的影子。',
'我想，我的心看到你了，欢快的跳动着。看到你的个签我会以为这是对我说的。我不愿想这是自作多情。是我恋上你了。',
'初恋像柠檬，虽酸却耐人寻味；热恋像火焰，虽热却不能自拔；失恋像伤疤，虽痛却无法释怀。所以我们要懂得呵护爱情！',
'繁星点点跨越银河能否与你相见？不怕遥远只盼此刻在你身边。往事如烟魂牵梦萦增添我的思念，追寻万年今生情缘不变。',
'生活是面包，爱情是奶酪，没有奶酪的面包一样能吃饱，就是味道不怎么好；没有爱情的生活也一样继续，就是不怎么美好。',
'寻寻觅觅这么久，终于让我遇到了你！这次我一定会拉着你的手，不会放开的，我会陪你一直走下去的，走属于我们的人生！',
'把你的名字写在手心，摊开时是想念，握紧时是幸福。就想这样，手牵手给你一世的温柔；就想这样，肩并肩给你一生的幸福！',
'东南西北寻找你，前后左右跟住你，春夏秋冬爱恋你，风雨雷电抱紧你，每天只想恋着你，今生今世爱着你，来世还是这顺序！',
'你是我的天空，时晴时雨；你是我的风景，山水相依；你是我的梦境，梦中有你；你是我的动力，让我进取。爱你，亘古不变！',
'迷失在大海的浪花上，踩在沙滩上，听着海风吹过耳边，闻着大自然的味道，和你牵手走过每一个地方，留下那一行一行的脚印。',
'我希望是阳光，让你倍加需要；我希望是氧气，让你快乐呼吸；我希望是玫瑰，让你人生美丽；我希望是短信，替我说声：想你！',
'遇见你，是我一生的幸运；爱上你，是我一生的快乐；失去你，是我一生的遗憾；没有你，无法感受心灵的震撼。此生惟愿爱你！',
'远处天边泛起了微光，我在等待中沉思，只想好好和你在一起，希望和你慢慢变老，枕着你宽大有力的肩膀走过每一个春夏秋冬！',
'你说你是一只披着羊皮的狼，那我就是那只被狼圈养的小羊。即便知道我只是你的一顿午餐，你仍是我的四月蒹葭，爱恋依然苍苍。',
'瓶爱瓶的塞，锅爱锅的盖，轮爱轮的胎，有你我就爱，蓝天上边有云彩，兔子爱白菜。天生一对不能改，至死不渝就是对你爱爱爱。',
'对于我来说，你就是命中注定。自然而然的牵起你的手，自然而然的用你入怀，你是独一无二的存在。我不懂说我爱你，但是需要你。',
'给我一百万个恋恋不舍的白天也觉不够，给我一辈子温馨浪漫的夜晚还嫌太少，和你在一起总觉得世界无法看透，永远不会有尽头……',
'亲爱的，你走的这些天很想你，感觉时间过得好慢，生活好无聊，总是不自觉的就想起你对我的好，我会一直乖乖的等你，等你回来！',
'每晚睡前，我都复习你花儿一样的容颜，月亮圆了又缺，缺了又圆，从没间断对你的思念。真心实意告诉你，我生命里的女主角就是你！',
'一见钟情是爱的端睨，两情相悦是爱的开始，将心比心是爱的进程，心心相印是爱的升华，天长地久是爱的承诺，白头偕老是爱的结局！',
'最难过的是遇见了，得到了，又匆忙的失去。然后在心底留了一道疤，它让你什么时候疼，就什么时候疼——送给那个留在我心底的你！',
'一生至少该有一次，为了某个人而忘了自己，不求有结果，不求同行，不求曾经拥有，甚至不求你爱我。只求在我最美的年华里，遇到你。',
'空气中迷茫着你留下的阵阵花香，雨静静的下看着你们顽皮的在雨中翩翩起舞，好像和你漫步在雨中在那阵阵花香中留下属于我们的爱的足迹。',
'山郎润了远方，水轻柔了夏夜，你滋润了时光，不知不觉已踏入十里红尘，阅尽繁华你是我最初的浑然天成，时光荏苒你是我唯一的心灵归宿。',
'一句承诺一世情，一生守候一颗心，一声问候一天暖，一份思念永延绵，一个想念你的我，在等着你的回信，愿我的存在，让你更加快乐幸福！',
'在这宁静的夜晚，思念已溢满我整个心房。不奢求你也是这样的想念我，只求你会偶尔的记起我，哪怕只是扫过脑海的一刹那，因为我依然爱你！',
'真真的心，想你；美美的意，恋你；暖暖的怀，抱你；甜甜的笑，给你；痴痴的眼，看你；深深的夜，梦你；满满的情，宠你；久久的我，爱你！',
'只有懂得生活的人，才能够感受生活中的美好，只有懂得爱的人，才能领略爱的真谛！今天我用心去默默想你，永远爱你感谢你走进了我的生活。',
'总是时常翻看短信，看着你发来的每一句问候，想着你当时的表情，心中也充满了甜蜜，傻傻的看着手机，心神却早已飞向你那，与你不离不弃。',
'你是我生活中最绚烂的眷恋，你的欢笑是我年华奔腾的追求，想告诉你一个转身我就在你身边，想告诉你我会陪你到爱的天堂。亲爱的，我想你了！',
'如果你是黄河，我就是其中的一滴水，如果你是恒山，我就是山顶的一粒沙；如果你是一碗刀削面，我……就要吃了你！哈哈！亲爱的，我的爱人。',
'一点爱一点情，日子甜甜又蜜蜜。一个我一个你，生活平淡不嫌腻。粗茶淡饭，吃出健康身体，简单衣着，也能万种风情。幸福有你，如此心心相印！',
'在分别的日子：想你，是我生命中最美的风景；想你，是我生活中不可或缺的音符；想你，如流沙曼舞离不开风。今生别无他求，只想与你相伴一生！',
'短信没到，你就迫不及待的偷看，想我了是不？别不承认，还笑！唉，明明是想我了，还不主动理我！伤心！还是我先想到你吧！亲爱的，真的好想你！',
'感谢老天给我们相遇，相知的机会。虽然不在一起了，但是不要忘了，你的世界我曾经来过！等你找到幸福的那一天，请不要忘了有一个人永远爱着你！',
'亲爱的，没事的时候我常常想你，想想你的可爱，你的笑容。想想你的野蛮，你的任性。想想我们在一起的快乐时光。一切都那么安好，宝贝，我爱你。',
'轻逸绝尘的你落在我的身旁，清澈的眼眸一丝浅笑让我心发慌，你在我的世界中央照耀我们梦幻的前方，给我无尽的未来力量。想告诉你，你是最好的！',
'为爱悄悄躲开，躲开的是身影，躲不开的是默默的关怀。月光下踯躅，睡梦里徘徊，对你的爱你何时明白？不是不去爱，不是不想爱，爱你在心口难开！',
'想告诉你我会给你浪漫和温馨，给你如影随形的贴心，给你一场为之动容的爱情，让我们一起编织未来的风景，一起享受爱情的纯真。我要给你最好的！',
'花好月圆不及你的倾心一笑，美轮美奂形容不出你的美丽，壮丽山河不如与你白头偕老，游山玩水更似人间无数，亲爱的，无论何时，我宁负天下不负卿。',
'绿水潺潺，倒影着你的身影；艳阳高照，闪耀着你的微笑；细细聆听，清风捎来浓浓思念；祝福传递，短信送来我的心愿。我愿与你携手相伴，幸福到老！',
'漫长的夜，自己痴痴地在想着你，久久不能睡去，梦带着我的心飞到你的身边，在你额头轻吻，和你携手相牵，只因你不在身边，才感觉今夜真的好想你！',
'诺言也许诚挚，在一起才最重要；时光也许仓促，你陪伴就最美好；回忆纵使美妙，你的气息最芬芳；未来也许挫折，紧握双手就心安。爱你不止在当下！',
'亲爱的，我喜欢紧紧抱着你，那一刻你的心在我的怀里跳动，我的双手停留在你的腰际，那一刻我抱着你的感觉，就像得到了整个世界。宝贝，我想你了。',
'想你的时候，打开相册，看着照片上你的笑容，回忆我们的点点滴滴；念你的时候，看看短信，想着你说过的每一句话，珍藏快乐的回忆。宝贝，我爱你。',
'那么遥远的外太空，卫星都已经对接成功了，那么我们这短短的异地恋又算得了什么呢？亲爱的，你要相信我们的爱情也能经得起距离和时间的考验，爱你！',
'有你在的日子，我希望可以每天陪着你，一起踏遍每个角落，你不在身边的日子，我的思念依旧那么没日没夜。片刻的安静，思绪是随你增长的魅力。我爱你。',
'于千千万人海中我找到了你，我要紧紧抱着你，我要用无微不至的爱珍惜你对我的好，用义无反顾的情滋润你生活的每个角落，祈福我们未来的每一个明天。',
'爱情，发乎心动，得之感动，持之信任，永恒于十指相扣，不离不弃。那样的爱情，不必要轰轰烈烈，不必要感天动地，只要前行时，一旁的人一直微笑追随。',
'爱情就像沙子，你握的越紧，它流失的越快。假如放松手指，沙子的流失会变得温和缓慢，直到静止。爱情也是如此，给爱一点空间，爱情仍会如蜂蜜般甜蜜。',
'爱一个人，有时是一辈子的事。爱一个人，有时只是一个阶段的事。学会取舍，淡然地面对每一份情感。拥有是福，放弃也是种拥有，得之我幸，不得亦我幸！',
'本来正常的天，忽然下起了雨；本来平静的夜，转瞬刮起了风；本来熟睡的人，成真了一个美梦；本来无助的我，拥有了一个你；一切都是缘份，所有都是命运。',
'不要轻易放弃一个每天都会想念的人。这样的人，一辈子也不会遇到几个。即便在一起要吃很多苦头，咬咬牙也就过去了。失去挚爱的疼痛，时间也无法洗涤。',
'大慨你还没睡醒，还在熟睡美梦中…我坐床上又想你，表声秒秒心动随…心动心跳相思随，仿佛床前守候你，爱护守护心贴心…待你醒来望窗外，旭日放光辉！',
'地球对太阳不舍昼夜的围转，是对它的不离不弃；海水接受月亮对自己潮汐的影响，是对它阴晴圆缺的包容。我对你的心，也是如此，永远不离不弃不怨不恨！',
'发柔飘舞秀长长，眼睛亮黑闪莹光…笑容纯纯动人美，话语悦耳终难忘…颜俊娇艳惊世俗，姿柔体雅真漂亮…外秀内慧真善美，感人动人舒心房…你神采风扬！',
'黄叶凋零，那个夏天并不遥远；白云苍狗，那段时光并不朦胧；忆往昔，二十四桥明月夜，卡瓦格博雪晶莹；感今朝，你依然是我的唯一，你依然是我的最爱。',
'蓝蓝的白云天，悠悠的河边柳…情侣牵手岸上走，喜上眉稍乐心头…阳光灿烂照耀你脸，红润含笑你温柔…彼此暗恋情缠绵，想说我爱你羞出口…相思在心头…',
'那种嘴上说爱，其实离你越来越远的，不过是谎言。那种满嘴真爱，其实一点亏都不肯吃的，无非是路过。真爱，就是奔结果去的。陪你到最后的，才是真爱。',
'你的微笑，是我奋斗的不竭动力，你的眼泪，是我悲伤的源泉。因此我只会让你微笑，让你幸福地笑。用我的全部精力呵护你，珍惜你。亲爱的，我好想你啊。',
'亲爱的，是你让我的心花团锦簇馨香缭绕，快乐和幸福一定会围绕着我们，就像左手挽住黄昏，右手挽住黎明。放心有我在，一切都会好的。宝贝，我想你了。',
'亲爱的，虽然不过节日，但我仍然想给你深情的问候，我要用一生来疼爱你。虽然你不在我的身边，但我时刻都把你放在心里最重要的位置。宝贝，我好想你！',
'亲爱的，我总盼望着有那么一天，我们一起早早起床，共吃早餐，出门上班，下班回家，买菜做饭，共看电视，甜蜜入睡。这就是我的梦想。宝贝，我想你了。',
'青春，终是逃不过一场爱情。爱情，也许是初见时那字斟句酌的思量，回首时那泪满衣襟的感慨；也许是欢愉时没心没肺的大笑，或是分离时撕心裂肺的痛哭。',
'青山绿水，传达绵绵思意。珠穆朗玛峰上有多少颗沙粒就代表我有多么想你！尼亚加拉瀑布有多少激流就表示我的心有多汹涌澎湃的爱意。我愿与你携手共进！',
'清晨睁开双眼，第一个想到的是你，你的笑容在我的脑海绽放，夕阳西下，我想念的还是你，你的话语还在我的耳畔环绕，亲爱的，我只想对你说：我想你了。',
'深夜，对你的思念开始肆无忌惮，想牵着你的手，闭着眼睛跟我一起幸福地走。我们的爱情就像洋葱，一片片剥下去，总有一片能让你感动地流泪。我想你了！',
'我承担不起宝马的速度，只能用单车载你游天下，我也永远和高楼别墅无缘！我们只能偎依在简单温馨的小屋内谈天说地！但我相信，有你陪伴，就是一生幸福。',
'我的脑海内存已满，美好被复制黏贴，都是你的贤惠体贴，善良温柔，灿烂未来已绘好，恩爱的我们，温馨的家，其乐融融。宝贝，我很期待那一刻的到来啊！',
'我们的双手相牵就不再分开，我们的拥抱只给人温暖安心，我们的誓言一起走到两鬓斑白步履蹒跚，我们约定每一个来生都要相伴。亲爱的，我觉得我很幸福。',
'我想告诉你我心里只有你一个人，只疼爱你一个人，时刻只想着你，有好吃的只给你吃，你需要的时候第一个出现，你到哪我就到哪。亲爱的，你是我的唯一！',
'想为你画个小圈，圈中间围着俩人…俩人感情像鞋条，系的紧紧在一块…想着打个坎肩儿，温暖度过最冷天…不求名利和享受，相依为命乐天天…情真爱永远！',
'曾经每天都很平淡，你使日子变得多滋味，工作感觉很枯燥，你使我变得干劲足，做饭总是要辛苦，但为你我不觉得累。宝贝，告诉你个秘密生活因你而美好。',
'每天晚上闭上眼就会想你梦到我们手牵手一起走，每天早上睁开眼就想看到你清澈甘甜的眼眸，每每想到你我就感觉幸福甜蜜陶醉不已。亲爱的，今天过的好吗？',
'喜欢你或许只是一瞬间的事情，这是这个过程很漫长，爱上你或许是很漫长的事，只是这种感觉却那么快。不要随便放开牵起我的手，只想这样与你一直走下去。',
'清晨的第一件事就是打开手机，对着手机屏幕，看着屏幕上你的一颦一笑，就好像你时时刻刻都在我的身边，陪我一同完成每日的各种工作，老婆，我想你，爱你。',
'亲爱的，对你的爱不会因距离而遥远，不会因时间而模糊。距离给了你我相互信任的基石，时间给你你我真爱永远的理由，宝贝，我的心一直为你而停留，今天我很想你。',
'想和你一起做的开心事就是慢慢变老，对你说的甜言蜜语一辈子都说不完。亲爱的，你要是有一点点不开心一定要告诉我啊，我就是为了取悦你的。你若安好，我就安心。',
'有你，有我，还有便是一单脚，相互，永久的走上去，不断走到地的边际，海的止境。或许那时我小了，头收黑了，己也没有帅了，但是我的脚不会抓紧，由于，我爱你。',
'有一种相遇，不是在路上，而是在心里；有一种感情，不是朝夕厮守，而是默默相伴；有一种语言，不必出声，却字字心声；有一种力量，没有施加任何推力，却在勇往直前。',
'我想要一份简单的爱情，日出而作，日落而息；一同享受每天清晨的阳光，微风，雨露，黄昏；这样的愿望，算不算贪心？我想爱情，就是相濡以沫的过一生。我想幸福，就是与你平平淡淡过一生。',
'青草青青，陌路几人行？轻风轻轻，相知多少情？一水浮萍，难守红蜻蜓；两声钟罄，惊飞黄头莺。夜深月明，只听夏虫鸣；睡迟梦凌，又见寒窗影。不胜酩酊，呓语解娉婷；何苦憧憬，醉影绊寂静。',
'请别放开，花的牵绊，将我的爱攥在手心；请别忘记，花的约定，将我的情融入心底；触念无边的思念，素描相思的痕迹，济济红尘里，满是你笑意，缘分的给予，我会倍加珍惜，任天荒地老有时尽，',
'我相信，总有那么一天你会捧着一束玫瑰为我单膝跪下，许下一辈子爱我照顾我的誓言，为我戴上那颗美丽的戒指，我相信，总有那么一天，我们虽已白发苍苍，你却依然拉着我的手，对我说：老伴，我爱你！',
'在我人生的旅途中，多少过客与我擦肩而过，而我为了寻觅你的到来而艰难跋涉，我就这样默默地一直把你守候，等待你路过我心灵驿站的那趟列车，你的停靠就是我最幸福的时刻，今生有你，就是我最大的福分与快乐！',
'牵手走过爱情的花园，沉浸在醉人的花香，喁喁而语浅笑嫣然，你的一颦一笑，拨动我的心弦，若能每日面对你的笑颜，却胜似天上人间，纵然是时光荏苒，真爱永不改变，缘起本是偶然，幸福却是必然！愿与你牵手幸福一生。',
'如果你问我每天想你多久？我会说想你三次，早上，中午，晚上。如果你问我会爱你多长？我会说爱你一辈子。如果你问我会照顾你多久？我会说照顾你四季，春天，夏天，秋天，冬天。亲爱的，和你在一起的每一天都是晴天。',
'风吹乱我前进的方向，指向你出现的地方。一见钟情的力量，把你记在了我的心上。事实傻傻的想像，能够享受到你的善良。总是徘徊在你的身旁，希望你能发现这个异常。将你带进我的世界飞翔，把所有伤心遗忘，让幸福地久天长！',
'不管花开花落，有你就有美好的生活；且看云卷云舒，有你是我一生的幸福。细碎时光，悠长岁月，爱如参天树，开出甜蜜花。茶，要喝浓的，直到淡而无味。酒，要喝醉的，永远不想醒来。人，要深爱的，要下辈子还要接着爱的那种。',
'让心成为一片海，懂得包容，方可自在。经历之后，才会懂得，真正的爱情不是海誓山盟，风花雪月，而是我和你在一起，没有大风大浪，有的只是平凡相依；经历之后，才会懂得，最爱的一直都是你，你的幸福快乐是我今生最大的心愿。',
'懂你的人，会用你所需要的方式去爱你。不懂你的人，会用他所需要的方式去爱你。于是，懂你的人，常是事半功倍，他爱得自如，你受得幸福。不懂你的人，常是事倍功半，他爱得吃力，你受得辛苦。两个人的世界里，懂比爱，更难做到。',
'幸福就是，陪你走一条叫一辈子的路，也许会累，会疲惫，却从没想过放弃；也许沿途风景迷人充满诱惑，却彼此保留住最初的感觉；也许会起争执，会有分歧，却依然会听从和默认；也许不能没分每秒在一起，却在心里始终留着一个位置。',
'爱我，就给我你的手，我会牵着它，永远到白头；爱我，就给我你的心，我会把它和我的心连在一起，我们永远不孤独；爱我，就给我你的泪，我会轻轻的为你擦干，抚去你的忧愁；爱我，就给我你的人，我让你躺在我怀里，细诉我们的幸福。',
'当我们变老，我们还是互相挽着手臂，走在长长的路上，就像我们已经搀扶着走过的几十个春秋；当我们变老，我们还是喜欢坐在长椅上，回想年轻时的故事；当我们变老，还是要握紧你的手，因为，那时候，我们说好了：牵手，一起慢慢变老。',
'爱，最需要的是舒坦。如果感觉自由舒服安心，你就爱对了；如果感觉处处被掣肘受控制没了自我，就该考虑调整了。爱，是互相依靠，相互温暖，相伴鼓励走向未知的未来。如果感觉在进步在成长那就对了；如果，感觉累反而没了方向，那就该调整了。',
'你穿高跟穿累了，我背你；你鞋带松了，我来绑；你不想吃饭，我来喂；你想结婚了，我来娶；你生气，我来哄；你想白头到老，我陪你；你想我爱你，可以，每天付出一点点，我们不需要什么天长地久，只要每天都住在对方的心里，我们就不会分开了！',
'我要做个拍卖师，为你拍卖琐碎烦恼；我要做个策划师，为你策划快乐微笑；我要做个建筑师，为你建造成功城堡；我要做个会计师，为你计算财富珍宝；我要做个护理师，为你呵护健康美妙；我要做个营养师，为你烹调幸福味道，夏日阳光妙，愿你一切好！',
'你是一朵报春花，春意盎然满枝丫；你是一支百合花，百年好合共天涯；你是一枚月季花，浓香馥郁显优雅；你是一盆水仙花，纯真情爱来表达；你是一束玫瑰花，一往情深传佳话；你是一片合欢花，恩爱百年情无暇；你是我的百花园，我做园丁呵护你到永远！',
'一辈子的爱，不是一场轰轰烈烈的爱情，也不是什么承诺和誓言。而是当所有人都离弃你的时候，只有TA在默默陪伴着你。当所有人都在赞赏你的时候，只有TA牵着你的手，嘴角上扬，仿佛骄傲的说，我早知道。时间会告诉你——越是平凡的陪伴，就越长久。']
# greetList = ['何渣渣','渣渣何','战斗力五的何渣渣','我陶恒是不是岳麓山第一狄仁杰，你说','我陶恒是不是岳麓山第一曹操，你说','我陶恒是不是岳麓山第一妲己，你说']
def tick():
    users = itchat.search_friends(name=u'七七') # 找到你女朋友的名称
    userName = users[0]['UserName']
    meetDate = dt.date(2012,4,22)  # 这是你跟你女朋友相识的日期
    now = dt.datetime.now()     # 现在的时间
    nowDate = dt.date.today()  # 今天的日期
    passDates = (nowDate-meetDate).days # 你跟你女朋友认识的天数
    itchat.send(u'今天是我们在一起第%d天，%s, 亲亲小媳妇'%(passDates,random.sample(greetList,1)[0]),toUserName=userName) # 发送问候语给女朋友
#     itchat.send(u'就问你服不服，%s'%(random.sample(greetList,1)[0]),toUserName=userName) 
    nextTickTime = now + dt.timedelta(days=1)
#     nextTickTime = now + dt.timedelta(seconds=2)
    nextTickTime = nextTickTime.strftime("%Y-%m-%d 00:00:00") 
    my_scheduler(nextTickTime) # 设定一个新的定时任务，明天零点准时问候
def my_scheduler(runTime):
    scheduler = BackgroundScheduler() # 生成对象
    scheduler.add_job(tick, 'date', run_date=runTime)  # 在指定的时间，只执行一次
    scheduler.start()
    
if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=-2,hotReload=True) # 在命令行中展示二维码，默认展示的是图片二维码
#     itchat.login()
#     itchat.auto_login(hotReload=True) # 这个是方便调试用的，不用每一次跑程序都扫码
    now = dt.datetime.now() # 获取当前时间
#     nextTickTime = now + dt.timedelta(days=1) #下一个问候时间为明天的现在
    nextTickTime = now + dt.timedelta(seconds=2)
#     nextTickTime = nextTickTime.strftime("%Y-%m-%d 00:00:00") # 把下一个问候时间设定为明天的零点
    my_scheduler(nextTickTime) # 启用定时操作
    itchat.run() # 跑微信服务
