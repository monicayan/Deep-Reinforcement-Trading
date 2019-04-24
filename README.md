# Deep-Reinforcement-Trading
Deep Reinforcement Learning driven trading agent.



This project is an implementation of Q-learning applied to stock trading. The agent uses n-day windows of closing prices to determine the best action at a given time is to buy, sell or sit.

This is agent is good as predicting peaks and troughs in short-term and not very good at making decisions over long-term trends, but is quite good at predicting peaks and troughs.



### Results

Some of the results are shown below:

![image](/images/^GSPC_2015.png)

Total profit: $ 972.43



![image](/images/^GSPC_2018.png)

Total profit: $1243.72



![image](/images/AMZN_2018.png)

Total profit: $1945.50



![image](/images/FB_2018.png)

Total profit: -$178.58



### Running Instruction

##### Data Preparation

setup the `data` folder and download historical dataset from [Yahoo/finance](https://ca.finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC) into `data` folder

```shell
mkdir data
```

##### Training

setup the `model` folder where we save our trained models, starting training with `python train.py [stock_name] [window_size] [epochs]` 

```shell
mkdir model
python train.py ^GSPC 10 1000
```

##### Evaulation

setup `plots` folder where we save our evaluate plots, run evaluate script with command `python evaulate.py [stock_name] [model_name]`

```shell
mkdir plots
python evaluate.py ^GSPC_2018 model_ep500
```



### Reference

[Deep Q-Learning with Keras and Gym](https://keon.io/deep-q-learning/) - Q-learning overview and Agent skeleton code

