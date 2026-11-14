def kmp(text, pattern):
    """Находит все начала вхождений pattern в text (в том числе пересекающихся).
    Время: O(n + m), память: O(m).
    """
    n = len(text)
    m = len(pattern)
    matches = []

    if m == 0 or m > n:
        return matches

    # ШАГ 1. Префикс-функция шаблона.
    # pi[i] = длина самой длинной границы строки pattern[0..i]
    # (префикс, который совпадает с суффиксом).
    pi = [0] * m
    k = 0                                   # текущая длина границы
    for i in range(1, m):
        while k > 0 and pattern[i] != pattern[k]:
            k = pi[k - 1]                   # откат к более короткой границе
        if pattern[i] == pattern[k]:
            k += 1                          # граница выросла на 1
        pi[i] = k

    # ШАГ 2. Поиск в тексте.
    # q = сколько символов шаблона сейчас совпало.
    q = 0
    for i in range(n):
        # Символ не подошёл: откатываем q, но указатель i назад НЕ двигаем.
        while q > 0 and text[i] != pattern[q]:
            q = pi[q - 1]
        # Символ подошёл: совпадение стало длиннее.
        if text[i] == pattern[q]:
            q += 1
        # Шаблон совпал целиком.
        if q == m:
            matches.append(i - m + 1)       # индекс начала вхождения
            q = pi[m - 1]                   # готовимся к пересекающимся вхождениям

    return matches


if __name__ == "__main__":
    text = "ABABABCABABCABAB"
    pattern = "ABABCABAB"

    print("Вхождения шаблона:", kmp(text, pattern)) 