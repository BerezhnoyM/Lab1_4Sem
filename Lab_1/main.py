def gen_bin_tree(height: int, root: int) -> dict:
    """ рекурсивная функция """
    if height == 1:
        return {root: []}
    else:
        left_leaf = (root + 1)
        right_leaf = (root - 1)
        left = gen_bin_tree(height - 1, left_leaf)
        right = gen_bin_tree(height - 1, right_leaf)
        return {root: [left, right]}


def main():
    if __name__ == '__main__':
        print('введите значения аргументов height и root')
        arg_height = input()
        arg_root = input()
        if arg_height != '' or arg_root != '':
            print(gen_bin_tree(int(arg_height), int(arg_root)))
        else:
            print('Вы не ввели значения. Были использованы стандартные аргументы \nheight = 3 \nroot = 13')
            print(gen_bin_tree(3, 13))


main()
