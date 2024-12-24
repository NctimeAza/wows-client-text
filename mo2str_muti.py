import polib
import os
import json

def mo_to_json(mo_file_path, output_json_path):
    """
    将 .mo 文件转换为 JSON 文件，格式为 {"id": "文本"}

    :param mo_file_path: 输入的 .mo 文件路径
    :param output_json_path: 输出的 .json 文件路径
    """
    try:
        # 读取 .mo 文件
        mo_file = polib.mofile(mo_file_path)

        # 创建一个字典来存储 id 和文本
        mo_dict = {entry.msgid: entry.msgstr for entry in mo_file}

        # 将字典写入 JSON 文件
        with open(output_json_path, 'w', encoding='utf-8') as json_file:
            json.dump(mo_dict, json_file, ensure_ascii=False, indent=4)

        print(f"转换完成！已将 {mo_file_path} 转换为 {output_json_path}")
    except Exception as e:
        print(f"转换失败：{e}")

def process_directory(input_dir, output_dir):
    """
    遍历指定目录下的 .mo 文件并转换为 JSON 文件。

    :param input_dir: 包含 .mo 文件的根目录
    :param output_dir: 输出的 JSON 文件保存目录
    """
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file == "global.mo":
                # 计算语言缩写（`LC_MESSAGES` 之前的目录名）
                relative_path = os.path.relpath(root, input_dir)
                language = relative_path.split(os.sep)[0]  # 提取语言缩写

                # 构造 .mo 文件路径和输出 JSON 文件路径
                mo_file_path = os.path.join(root, file)
                output_json_path = os.path.join(output_dir, f"{language}.json")

                # 创建输出目录（如果不存在）
                os.makedirs(output_dir, exist_ok=True)

                # 执行转换
                mo_to_json(mo_file_path, output_json_path)

if __name__ == "__main__":
    # 输入和输出根目录
    input_directory = os.path.join(os.getcwd(), "texts")  # 修改为你的输入目录
    output_directory = os.path.join(os.getcwd(), "output")  # 修改为你的输出目录

    # 执行目录处理
    process_directory(input_directory, output_directory)
