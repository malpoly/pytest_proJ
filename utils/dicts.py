def get_val(collection, keys, default='git'):
    """
        Извлекает из словаря по переданному ключу, если ключ существует.
        Если ключ не существует, возвращает значение по умолчанию.
        Функция работает только с неотрицательными индексами.
        :param collection: исходный словарь.
        :param key: ключ извлекаемого элемента.
        :param default: значение по-умолчанию.
        :return: значение по ключу ли значение по-умолчанию.
        """
    default = 'git' if default is None else default

    for key, item in collection.items():
        if key == keys:
            return item
        else:
            return default

    length = len(collection)
    if length == 0:
        return default



