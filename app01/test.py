#!/usr/local/python3


from transformers import AutoModelForCausalLM, AutoTokenizer, Conversation

# 加载 ChatGPT 模型和 Tokenizer
model_name = "microsoft/DialoGPT-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 定义一个对话
conv = Conversation()

# 定义 ChatGPT 的 interaction 配置项
interaction = model.config.interaction_control

# 设置 share_context 参数为 True，表示共享对话上下文
interaction.share_context = True
model.config.interaction_control = interaction

# 给 ChatGPT 机器人输入一句话，并获取回复
input_text = "Hi, how are you?"
input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
bot_output = model.generate(input_ids)

# 将机器人的回复加入到对话中
bot_reply = tokenizer.decode(bot_output[0], skip_special_tokens=True)
conv.add_user_input(input_text)
conv.add_bot_output(bot_reply)

# 打印当前对话的上下文
print(conv.context)

# 设置 share_context 参数为 False，表示不共享对话上下文
interaction.share_context = False
model.config.interaction_control = interaction

# 给 ChatGPT 机器人输入另一句话，并获取回复
input_text = "What's your favorite movie?"
input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
bot_output = model.generate(input_ids)

# 将机器人的回复加入到对话中
bot_reply = tokenizer.decode(bot_output[0], skip_special_tokens=True)
conv.add_user_input(input_text)
conv.add_bot_output(bot_reply)

# 打印当前对话的上下文
print(conv.context)



