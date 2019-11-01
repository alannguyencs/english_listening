import codecs
from constants import *
from string_handler import string_handler

class Processor():

    def procedure(self):
        self.script_content = self.parse_data_file(SCRIPT_PATH)
        self.typing_content = self.parse_data_file(TYPING_PATH)
        self.lcc_content = string_handler.longest_common_child(self.script_content, self.typing_content)

        self.error_in_script = string_handler.get_marking_error(self.lcc_content, self.script_content)
        self.error_in_typing = string_handler.get_marking_error(self.lcc_content, self.typing_content)

        self.matching_score = self.get_matching_score()
        self.show_result()

    def get_matching_score(self):
        return 2 * len(self.lcc_content) / (len(self.script_content) + len(self.typing_content))

    def show_result(self):
        result_message = "Matching score = {:.2f}%\n\n".format(100 * self.matching_score)
        result_message += "Your typing:\n{}".format(string_handler.convert_list_to_string(self.error_in_typing))
        result_message += "\n\nScript:\n{}".format(string_handler.convert_list_to_string(self.error_in_script))

        error_file = open(RESULT_PATH, 'w')
        error_file.write(result_message)
        print (result_message)

    def parse_data_file(self, file_path):
        data_file = codecs.open(file_path, 'r', 'utf8')
        file_content = []
        for line in data_file:
            line = line.strip()

            if len(line) == 0:
                continue

            raw_words = line.split()
            words = [self.remove_non_alpha_characters(word).lower() for word in raw_words]

            file_content += words

        return file_content

    def remove_non_alpha_characters(self, text):
        return ''.join(c for c in text if (c.isalpha() or c.isdigit()))




