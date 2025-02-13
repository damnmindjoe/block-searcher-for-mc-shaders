import json
import re
import os

# Основной скрипт
def process_local_file(file_path):
    # Открываем и читаем локальный файл
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except Exception as e:
        raise Exception(f"Ошибка при чтении файла: {e}")

    # Создаем папку для выходных файлов
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    # Словарь для группировки блоков по типам
    grouped_blocks = {}

    # Регулярное выражение для поиска блоков
    pattern = re.compile(r"block\.([a-zA-Z0-9_]+)\.([a-zA-Z0-9_]+)")

    # Обрабатываем все ключи в JSON
    for key in data:
        match = pattern.match(key)
        if match:
            mod_name = match.group(1)  # Название мода
            block_name = match.group(2)  # Название блока

            # Переформатируем в (название мода):(название блока)
            formatted_block = f"{mod_name}:{block_name}"

            # Группируем блоки по типу (например, grass, metal, glass)
            block_type = block_name.split("_")[0]  # Первая часть названия блока
            if block_type not in grouped_blocks:
                grouped_blocks[block_type] = []
            grouped_blocks[block_type].append(formatted_block)

    # Записываем результаты в файлы
    for block_type, blocks in grouped_blocks.items():
        output_file = os.path.join(output_folder, f"{block_type}.txt")
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(" ".join(blocks))

    print(f"Результаты записаны в папку {output_folder}.")

# Пример использования
if __name__ == "__main__":
    file_path = input("Введите путь к файлу en_us.json на вашем компьютере: ")
    try:
        process_local_file(file_path)
    except Exception as e:
        print(f"Ошибка: {e}")
