
class RuleParser(object):
    def __int__(self):
        pass

    def parse_if_then_rule(self, rule_str):
        word_list = rule_str.split(" ")
        n = len(word_list)
        val = []
        label = []
        input_dict = {}
        output_dict = {}
        for i in range (n):
            if word_list[i] == "is":
                val.append(word_list[i-1])
                label.append(word_list[i+1])
        n = len(val)
        for i in range (n - 1):
            input_dict[val[i]] = label[i]
        output_dict[val[n-1]] = label[n-1]
        return input_dict, output_dict






