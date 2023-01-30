# створюємо клас для обробки текстових даних
class TextProcessor:
# створюмо аргументи - знаки пунктуації
    def __init__(self):
        self._punktuation = '.,-!?;:*'

    def __is_punktuation(self, char):
        return char in self._punktuation

# публічний метод get_clean_string для видалення знаків пунктуації
    def get_clean_string(self, text):
        clean_text = ""
        for char in text:
            if self.__is_punktuation(char):
                continue
            clean_text += char
        return clean_text


#Створюєм клас TextLoader (мета - виведення повідомлення в консоль)
class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

#
    def set_clean_string(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

# додатковий property для clean_string для виведення повідомлення в консоль
    @property
    def clean_string(self):
        print("This text contains no punctuation marks: {}".format(self.__clean_string))
        return self.__clean_string

# Клас DataInterface (мета - опрацювання в циклі списку рядків і виведенню значення на екран)
class DataInterface:
    def __init__(self):
        self.__text_loader = TextLoader()

# публічний метод process_texts для опрацювання в циклі списку рядків і виведенню значення на екран
    def process_texts(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_string(text)
            clean = self.__text_loader.clean_string
            clean_texts.append(clean)
        return clean_texts


using_class = DataInterface()
sentence = ['Perhaps, although, it is not certain, but - for sure!, or not? *', 'And, of course, yes!']
final_text = using_class.process_texts(sentence)