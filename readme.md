# ChineseAiDungeon

中文版本的ai地牢，一个使用GPT-2的文字冒险游戏，使用清源CPM预训练模型finetune而成。 

![](imgs/demo.gif)

点击 [这里](https://colab.research.google.com/github/bupticybee/ChineseAiDungeon/blob/main/ChineseAiDungeonColabDemo.ipynb) 赶快在 google colab 上体验吧！

## 如何开始游戏
你可以选择直接在colab上[体验](https://colab.research.google.com/github/bupticybee/ChineseAiDungeon/blob/main/ChineseAiDungeonColabDemo.ipynb)  ，或者也可以将代码clone到本地，运行ChineseAiDungeonColabDemo.ipynb 文件进行游戏。

## 开始游戏前须知
- 游戏可以运行在cpu或者gpu上，但是cpu上的模型推断会非常漫长，不建议！
- 需要8GB以上的显存运行本程序
- finetune语料是经过google翻译的 Choose Your Story网站文本，由于经过翻译，质量本身并不好，目前不要对ChineseAiDungeon 生成的故事质量抱有太大期望

## 自己finetune模型

遵循 ```finetune.ipynb```文件中的步骤开始finetune，需要1张至少16GB显存的显卡。由于我的硬件限制，我只finetune了清源CPM的2.6B的fp16模型，并没有使用fp32的模型。我本人finetune后的模型地址在[这里](https://drive.google.com/file/d/1cJ1kvtPrV4TXxiadiGU6bJUAy11bRDm1).