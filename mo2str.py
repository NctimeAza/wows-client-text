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

if __name__ == "__main__":
    # 输入和输出路径
    mo_file_path = os.path.join(os.getcwd(), "global.mo")  # 修改为你的 .mo 文件路径
    output_json_path = os.path.join(os.getcwd(), "uk.json")  # 修改为输出的 .json 文件路径

    # 创建输出目录（如果不存在）
    os.makedirs(os.path.dirname(output_json_path), exist_ok=True)

    # 执行转换
    mo_to_json(mo_file_path, output_json_path)
