# zh-code-checker-ai-model v2

## 概述

zh-code-checker-ai-model v2 是基于 [hfl/rbt4-h312](https://huggingface.co/hfl/rbt4-h312) 模型的适用于 OI 系列比赛的 AI 代码检测模型。

v2 版本的模型在 v1 版本的基础上，对模型的训练数据集进行了扩充，同时对模型的训练过程进行了优化，提高了模型的检测准确率。

## 模型信息

我们使用 [hfl/rbt4-h312](https://huggingface.co/hfl/rbt4-h312) 模型作为基础模型，对其进行了微调，得到了 zh-code-checker-ai-model v2。

我们调用讯飞星火 Spark-Lite，生成了洛谷题库主题库与 B 题库的题目代码、AtCoder ABC 的百余场比赛的题目代码，作为 AI 代码的训练数据集。

同时，我们收集了全国各地 Oier 的代码，作为人类代码的训练数据集。

v2 版本的训练共包含 $12141$ 份 AI 生成代码，共 $13.3$MB，$5202127$ tokens；包含 $50193$ 份人类代码，共 $58.7$MB，$30861538$ tokens。

- train_loss: $0.03864411759469658$
- eval_loss: $0.023131858557462692$
- learning_rate: $3.1742051706509566 \times 10^{-5}$
