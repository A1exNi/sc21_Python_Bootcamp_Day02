from dataclasses import dataclass


@dataclass
class Key():
    ln: int = 0
    at: int = 0
    gt: int = 0
    passphrase: str = None
    string: str = None

    def __len__(self) -> int:
       return self.ln

    def __gt__(self, other) -> bool:
        return self.gt > other

    def __getitem__(self, key) -> int:
        if key == 404:
            return self.at
        else:
            return 0

    def __str__(self) -> str:
       return self.string


def test_len(key: Key):
    if len(key) == 1337:
        print('Test len: True')
    else:
        print('AssertionError: len(key) == 1337')


def test_at(key: Key):
    if key[404] == 3:
        print('Test access: True')
    else:
        print('AssertionError: key[404] == 3')


def test_gt(key: Key):
    if key > 9000:
        print('Test gt: True')
    else:
        print('AssertionError: key > 9000')


def test_passphrase(key: Key):
    if key.passphrase == 'zax2rulez':
        print('Test passphrase: True')
    else:
        print('AssertionError: key.passphrase == "zax2rulez"')


def test_str(key: Key):
    if str(key) == 'GeneralTsoKeycard':
        print('Test string: True')
    else:
        print('AssertionError: str(key) == "GeneralTsoKeycard"')


def main():
    tests = [test_len, test_at, test_gt, test_passphrase, test_str]
    print('======Неправильный ключ======')
    key: Key = Key(0, 0, 0, 'asdf', 'wer')
    for func in tests:
        func(key)
    print('---------------------------')
    print('======Правильный ключ======')
    key: Key = Key(1337, 3, 9001, 'zax2rulez', 'GeneralTsoKeycard')
    for func in tests:
        func(key)
    print('---------------------------')


if __name__ == '__main__':
  main()