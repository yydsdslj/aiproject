from ai_web_crawler.ai_web_crawler.chat import get_chat_response

def main():
    while True:
        # 获取用户输入
        prompt = input("请输入你的问题（输入 'exit' 退出）: ")
        if prompt.lower() == 'exit':
            break

        # 获取模型回答
        response = get_chat_response(prompt)
        if response:
            print(f"模型回答: {response}")

if __name__ == "__main__":
    main()
