# ChineseAiDungeon
<pre>

 .oooooo.   oooo         o8o                                           
 d8P'  `Y8b  `888         `"'                                           
888           888 .oo.   oooo  ooo. .oo.    .ooooo.   .oooo.o  .ooooo.  
888           888P"Y88b  `888  `888P"Y88b  d88' `88b d88(  "8 d88' `88b 
888           888   888   888   888   888  888ooo888 `"Y88b.  888ooo888 
`88b    ooo   888   888   888   888   888  888    .o o.  )88b 888    .o 
 `Y8bood8P'  o888o o888o o888o o888o o888o `Y8bod8P' 8""888P' `Y8bod8P' 
                                                                        
                                                                        
      .o.        o8o  oooooooooo.                                                                      
     .888.       `"'  `888'   `Y8b                                                                     
    .8"888.     oooo   888      888 oooo  oooo  ooo. .oo.    .oooooooo  .ooooo.   .ooooo.  ooo. .oo.   
   .8' `888.    `888   888      888 `888  `888  `888P"Y88b  888' `88b  d88' `88b d88' `88b `888P"Y88b  
  .88ooo8888.    888   888      888  888   888   888   888  888   888  888ooo888 888   888  888   888  
 .8'     `888.   888   888     d88'  888   888   888   888  `88bod8P'  888    .o 888   888  888   888  
o88o     o8888o o888o o888bood8P'    `V88V"V8P' o888o o888o `8oooooo.  `Y8bod8P' `Y8bod8P' o888o o888o 
                                                            d"     YD                                  
                                                            "Y88888P'                                  
                                                                                                               
</pre>

中文版本的ai地牢，一个使用GPT-2的文字冒险游戏，使用清源CPM预训练模型finetune而成。 

点击 [这里](https://colab.research.google.com/github/bupticybee/ChineseAiDungeon/blob/main/ChineseAiDungeonColabDemo.ipynb) 赶快在 google colab 上体验吧！

![](imgs/demo.gif)


## 如何开始游戏
你可以选择直接在colab上[体验](https://colab.research.google.com/github/bupticybee/ChineseAiDungeon/blob/main/ChineseAiDungeonColabDemo.ipynb)  ，或者也可以将代码clone到本地，运行ChineseAiDungeonColabDemo.ipynb 文件进行游戏。

## 开始游戏前须知
- 游戏可以运行在cpu或者gpu上，但是cpu上的模型推断会非常漫长，不建议！
- 需要8GB以上的显存运行本程序
- finetune语料是经过google翻译的 Choose Your Story网站文本，由于经过翻译，质量本身并不好，目前不要对ChineseAiDungeon 生成的故事质量抱有太大期望

## 模型

| 模型         | 文件大小 | 百度网盘地址                                         | google drive地址                                                                 | 备注                                          |
| -------------- | -------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------- |
| storyTeller1.1 | 4.8G     | https://pan.baidu.com/s/1OiRbMydElmISFtRW3k0y5Q 提取码awb7 | https://drive.google.com/file/d/1cJ1kvtPrV4TXxiadiGU6bJUAy11bRDm1/view?usp=sharing | 2.6B-fp16,使用经过翻译的chooseYourStory语料训练 |

## 自己finetune模型

遵循 ```finetune.ipynb```文件中的步骤开始finetune，需要1张至少16GB显存的显卡。由于我的硬件限制，我只finetune了清源CPM的2.6B的fp16模型，并没有使用fp32的模型。我本人finetune后的模型地址在[这里](https://drive.google.com/file/d/1cJ1kvtPrV4TXxiadiGU6bJUAy11bRDm1).
