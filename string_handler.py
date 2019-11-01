

class StringHandler():
    def longest_common_child(self, X, Y):
        m, n = len(X), len(Y)

        # declaring the array for storing the dp values
        lcc_length = [[None for _ in range(n + 1)] for _ in range(m + 1)]
        lcc_content = [[None for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    lcc_length[i][j] = 0
                    lcc_content[i][j] = ''

                elif X[i - 1] == Y[j - 1]:
                    lcc_length[i][j] = lcc_length[i - 1][j - 1] + 1
                    lcc_content[i][j] = lcc_content[i - 1][j - 1] + '|' + X[i - 1]

                elif lcc_length[i - 1][j] > lcc_length[i][j - 1]:
                    lcc_length[i][j] = lcc_length[i - 1][j]
                    lcc_content[i][j] = lcc_content[i - 1][j]

                else:  # lcc_length[i - 1][j] < lcc_length[i][j - 1]:
                    lcc_length[i][j] = lcc_length[i][j - 1]
                    lcc_content[i][j] = lcc_content[i][j - 1]

        lcc_content_ = lcc_content[m][n][1:].split('|')
        return lcc_content_

    def get_similarity_score(self, X, Y):
        lcc_content = self.get_longest_common_child(X, Y)
        similarity_score = 2 * len(lcc_content) / (len(X) + len(Y))
        return similarity_score

    def get_marking_error(self, child_content, parent_content):
        # print (parent_content)
        error_content = list()
        run_id = 0
        for id in range(len(parent_content)):
            if parent_content[id] == child_content[run_id]:
                error_content.append(parent_content[id])
                run_id += 1
                if run_id == len(child_content):
                    break
            else:
                error_content.append(parent_content[id].upper())

        return error_content

    def convert_list_to_string(self, list_content):
        MAX_WORDS_PER_LINE = 15
        content = ""
        for word_id, word in enumerate(list_content):
            content += word
            if word_id % MAX_WORDS_PER_LINE == MAX_WORDS_PER_LINE - 1:
                content += '\n'
            else:
                content += ' '
        return content

string_handler = StringHandler()